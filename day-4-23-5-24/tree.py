
class node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        newnode = node(data)
        if self.root == None:
            self.root = newnode
        else:
            curr = self.root
            while True:
                if curr.data <= data:
                    if curr.right == None:
                        curr.right = newnode
                        break
                    else:
                        curr =curr.right
                else:
                    if curr.left == None:
                        curr.left = newnode
                        break
                    else:
                        curr = curr.left
    def searchnode(self,data):
        s = self.search(self.root,data)
        if s!= None:
            print("Found")
        else:
            print("Not Found")
    def search(self,root,data):
        if root == None or root.data == data:
            return root
        else:
            return self.search(root.left,data) or self.search(root.right,data)
        
    
'''def preorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.data)'''
t = Tree()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(7)
t.insert(6)
inorder(t.root)
t.searchnode(4)
