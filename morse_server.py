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
    # Connecting to the server
    async with websockets.connect(uri) as websocket:
        # Receiving a message
        message = json.loads(await websocket.recv())
        # Encoding the message and passing "time" as receiver
        encoded_msg = ham_radio.encode_ham("time", sender,  "Hello")
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            # Adding the encoded message to a dictionary
            outward_message = {
                'client_id': client_id,
                "type": "morse_evt",
                'payload': encoded_msg,
            }
            # Sending the message to the server
            message = await websocket.send(json.dumps(outward_message))
            # receiving a response from the server
            message = json.loads(await websocket.recv())
            # Return last response from server
            return message['payload']
    return 0


async def send_echo(sender, msg):
    uri = "ws://localhost:10102"
    # Connecting to the server
    async with websockets.connect(uri) as websocket:
        # Receiving a message
        message = json.loads(await websocket.recv())
        # Encoding the message
        encoded_msg = ham_radio.encode_ham("echo", sender, msg)
        if message['type'] == 'join_evt':
            client_id = message['client_id']
            # Adding the encoded message to a dictionary
            outward_message = {
                'client_id': client_id,
                "type": "morse_evt",
                'payload': encoded_msg,
            }
            # Sending the message to the server
            message = await websocket.send(json.dumps(outward_message))
            # receiving a response
            message = json.loads(await websocket.recv())
            print(morse.decode(message))
            # Return last response from server
            return message['payload']
    return 0

# asyncio.run(send_time('s'))
asyncio.run(send_time('s'))
