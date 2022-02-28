
class Node:
    def __init__(self, data="Start", root=None):
        self.left = None
        self.right = None
        self.data = data
        self.root = root

    def looping(self, node, code, x, letter):
        if(code[x] == "-"):
            if(len(code) > (x+1)):
                if(node.right == None):
                    node.right = Node("blank", node)
                self.looping(node.right, code, x+1, letter)
            else:
                node.right = Node(letter)
        elif(code[x] == "."):
            if(len(code) > (x+1)):
                if(node.left == None):
                    node.left = Node("blank", node)
                self.looping(node.left, code, x+1, letter)
            else:
                node.left = Node(letter, node)

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
    
    def isEmpty(self):
        return self.data

    def find(self, value, tree):
        if(tree.data == value):
            print("Found")
            return True
        else:
            if(tree.left):
                boolLeft = self.find(value, tree.left)
                if(boolLeft):
                    return True;
            if(tree.right):
                boolRight = self.find(value, tree.right)
                if(boolRight):
                    return True;
        
        return False

    def deleteDeepest(root,d_node):
        q = []
        q.append(root)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

  
    # function to delete element in binary tree
    def delete(self, value):
        returnValue = self.search(value)
        if(returnValue != None):
            node = returnValue[0]
            par = returnValue[1]
            if(node.getLeft() == None or node.getRight() == None):
                if(node == self.root):
                    node = self.next(node)
                elif(par.left == node):
                    par.left = self.next(node)
                else:
                    par.right = self.next(node)
            else:
                arr = self.inOrderTraveral(self.root)
                index = arr.index(node)
                pre = arr[index]
                parpre = arr[index-2]

                print(parpre.getValue())
                # updaye the node's value
                if(par.left == node):
                    par.left = pre
                else:
                    par.right = pre

                # delete the predecessor
                if(parpre.left == pre):
                    parpre.left = pre
                else:
                    parpre.right = pre
        else:
            return None
        
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

print(root.find("-", root))

