import asyncio
import string
from typing import Type
import websockets
import json
import sys
import ham_radio
import morse

async def send_time(sender):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        message = json.loads(await websocket.recv())
        encoded_msg = ham_radio.encode_ham("time", sender,  "Hello")
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            outward_message = {
                'client_id': client_id,
                "type": "morse_evt",
                'payload': encoded_msg,
            }
            message = await websocket.send(json.dumps(outward_message))
            message = json.loads(await websocket.recv())
            return message['payload']
    return 0

# type: morse_evt
async def send_echo(sender, msg):
    uri = "ws://localhost:10102"
    async with websockets.connect(uri) as websocket:
        message = json.loads(await websocket.recv())
        encoded_msg = ham_radio.encode_ham("echo", sender, msg)
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            outward_message = {
                'client_id': client_id,
                "type": "morse_evt",
                'payload': encoded_msg,
            }
            message = await websocket.send(json.dumps(outward_message))
            message = json.loads(await websocket.recv())
            print(morse.decode(message))
            return message['payload']
    return 0

# asyncio.run(send_time('s'))
asyncio.run(send_time('s'))
