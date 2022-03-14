class Node:
    def __init__(self, data="Start"):
        self.left = None
        self.right = None
        self.data = data
    
    def isEmpty(self):
        return (self.left == None and self.right == None)
    
    def looping(self, node, code, x, letter):
        if(code[x] == "-"):
            if(len(code) > (x+1)):
                if(node.right == None):
                    node.right = Node("blank")
                self.looping(node.right, code, x+1, letter)
            else:
                if(node.right != None and node.right.data == "blank"):
                    node.right.data = letter
                else:
                    node.right = Node(letter)
        elif(code[x] == "."):
            if(len(code) > (x+1)):
                if(node.left == None):
                    node.left = Node("blank")
                self.looping(node.left, code, x+1, letter)
            else:
                if(node.left != None and node.left.data == "blank"):
                    node.left.data = letter
                else:
                    node.left = Node(letter)   

    def insert(self, letter, code):
        tempNode = self
        self.looping(tempNode, code, 0, letter)

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

    def delete(self, value, tree):
        if(tree.data == value):
            tree.data = Node()
            return True
        else:
            if(tree.left):
                boolLeft = self.delete(value, tree.left)
                if(boolLeft):
                    return True;
            if(tree.right):
                boolRight = self.delete(value, tree.right)
                if(boolRight):
                    return True;
        
    # Print the tree
    def PrintTree(self, position="root"):
        print(self.data, position),
        if self.left:
            self.left.PrintTree("left")
        if self.right:
            self.right.PrintTree("right")






# Use the insert method to add nodes
# root = Node()
# root.insert("E", "---...")
# root.insert("B", "-")
# root.PrintTree()
# root.insert(14)
# root.insert(3)
# data = [
#     ["E", "."],

#     ["I", ".."],
#     ["S", "..."],
#     ["H", "...."],
#     ["V", "...-"],
#     ["U", "..-"],
#     ["F", "..-."],

#     ["A", ".-"],
#     ["R", ".-."],
#     ["L", ".-.."],
#     ["W", ".--"],
#     ["P", ".--."],
#     ["J", ".---"],


#     ["T", "-"],

#     ["N", "-."],
#     ["D", "-.."],
#     ["B", "-..."],
#     ["X", "-..-"],
#     ["K", "-.-"],
#     ["C", "-.-."],
#     ["Y", "-.--"],

#     ["M", "--"],
#     ["G", "--."],
#     ["Z", "--.."],
#     ["Q", "--.-"],
#     ["O", "---"],
# ]

# root.PrintTree()
# print("\n\n\n")
# for x in data:
#     root.insert(x[0], x[1])
# root.PrintTree()

# print(root.delete("M", root))

# print(root.isEmpty())
# root.isEmpty()

