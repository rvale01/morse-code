from morse import encode 
from morse import decode

def encode_ham(receiver, sender, msg):
    newMsg = receiver + "de" + sender+ "=" + msg + "=("
    encodedMsg = encode(newMsg)
    return encodedMsg

def decode_ham(msg:str):
    decodedMsg = decode(msg)
    receiver, decodedMsg = decodedMsg.split("de")
    sender, message, useless = decodedMsg.split("=")
    return (receiver, sender, message)

# print(decode_ham(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."))
# print(encode_ham("r1", "s1", "hi"))