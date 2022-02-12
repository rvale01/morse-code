from tree import Node

def initNode():
    root = Node()
    data = [
        ["E", "."],

        ["I", ".."],
        ["S", "..."],
        ["H", "...."],
        ["V", "...-"],
        ["U", "..-"],
        ["F", "..-."],

        ["A", ".-"],
        ["R", ".-."],
        ["L", ".-.."],
        ["W", ".--"],
        ["P", ".--."],
        ["J", ".---"],


        ["T", "-"],

        ["N", "-."],
        ["D", "-.."],
        ["B", "-..."],
        ["X", "-..-"],
        ["K", "-.-"],
        ["C", "-.-."],
        ["Y", "-.--"],

        ["M", "--"],
        ["G", "--."],
        ["Z", "--.."],
        ["Q", "--.-"],
        ["O", "---"],
    ]

    for x in data:
        root.insert(x[0], x[1])
    return root


def loopEncode(node, char, result):
    if node == None:
            return False
    elif node.data==char:
        return True
    else:  
        if loopEncode(node.left,char,result)==True:
            result.insert(0,".")
            return True
        elif loopEncode(node.right,char,result)==True:
            result.insert(0,"-")
            return True

def encode(msg):
    msg = msg.upper()
    morseCode = ""
    node = initNode()

    #Convert the message, one character at a time!
    for character in msg:
        if(character != " "):
            result = []
            loopEncode(node,character,result)
            code = "".join(result)
            morseCode = morseCode + code  
            if(character != msg[len(msg)-1]):
                 morseCode = morseCode + ' '
        else:
            morseCode = morseCode + " "
        
    return morseCode
        
def decode(msg):
    msg = msg.split(" ")
    node = initNode()
    message = ""
    for x in msg:
        loop = True
        count = 0
        tempNode = node
        while(loop):
            if(x[count] == "-"):
                if(len(x) > (count+1)):
                    tempNode = tempNode.right
                    count = count + 1
                else:
                    loop = False
                    message = message + tempNode.right.data
            elif(x[count] == "."):
                if(len(x) > (count+1)):
                    tempNode = tempNode.left
                    count = count + 1
                else:
                    loop = False
                    message = message + tempNode.left.data
    return message.lower()

# encoded = encode("VALE")
# print(encoded)
# print(decode(encoded))