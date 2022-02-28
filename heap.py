class Heap:
    def __init__(self):
        self.heap = []
    def add(self, value):
        self.heap.append(value)

def initHeap(heap):
    morseList = "-,E,T,I,A,N,M,S,U,R,W,D,K,G,O,H,V,F,-,L,-,P,J,B,X,C,Y,Z,Q,-,-"
    morseList = morseList.split(",")
    for x in morseList:
        heap.add(x)

def loop_decode(sectionMsg, heap):
    index = 1
    for y in range(len(sectionMsg)):
        if( sectionMsg[y] == "."):
            index = 2*index
        else:
            index = 2*index + 1
        
        if(y == (len(sectionMsg) - 1)):
            return heap.heap[index -1] 

def decode_bt(msg):
    heap = Heap()
    initHeap(heap)
    msg = msg.split(" ")
    decoded_msg = ""
    for x in msg:
        if(x == "/"):
            decoded_msg = decoded_msg + " "
        else:
            decoded_msg = decoded_msg + str(loop_decode(x, heap))
    return decoded_msg.lower()


# decode_bt("-.-. --- -.. .. -. --.")