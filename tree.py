class Node:
    def __init__(self, data="Start", root=None):
        self.left = None
        self.right = None
        self.data = data

    def looping(self, node, code, x, letter):
        if(code[x] == "-"):
            if(len(code) > (x+1)):
                if(node.right == None):
                    node.right = Node("blank")
                self.looping(node.right, code, x+1, letter)
            else:
                node.right = Node(letter)
        elif(code[x] == "."):
            if(len(code) > (x+1)):
                if(node.left == None):
                    node.left = Node("blank")
                self.looping(node.left, code, x+1, letter)
            else:
                node.left = Node(letter)

    def insert(self, letter, code):
        tempNode = self
        self.looping(tempNode, code, 0, letter)
        # if self.data:
        #     if data < self.data:
        #         if self.left is None:
        #             self.left = Node(data)
        #         else:
        #             self.left.insert(data)
        #     elif data > self.data:
        #         if self.right is None:
        #             self.right = Node(data)
        #         else:
        #             self.right.insert(data)
        # else:
        #     self.data = data

    # Print the tree
    def PrintTree(self, position="root"):
        print(self.data, position),
        if self.left:
            self.left.PrintTree("left")
        if self.right:
            self.right.PrintTree("right")






# Use the insert method to add nodes
root = Node()
# root.insert(6)
# root.insert(14)
# root.insert(3)
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
# root.PrintTree()
