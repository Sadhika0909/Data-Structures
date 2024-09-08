#defining a tree
class Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data is None:
            self.data=data
        else:
            if data<self.data:
                if self.left is None:
                    self.left=Tree(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Tree(data)
                else:
                    self.right.insert(data)

def inorder(r):
    if r is None:
        return
    else:
        inorder(r.left)
        print(r.data,end=" ")
        inorder(r.right)

def preorder(r):
    if r is None:
        return
    else:
        print(r.data,end=" ")
        preorder(r.left)
        preorder(r.right)

def postorder(r):
    if r is None:
        return
    else:
        postorder(r.left)
        postorder(r.right)
        print(r.data,end=" ")

if __name__=="__main__":
    root=Tree("s")
    root.insert("h")
    root.insert("e")
    root.insert("w")
    root.insert("t")
    root.insert("n")
    root.insert("a")
    root.insert("l")
    root.insert("p")

print("Inorder traversal: ")
inorder(root)
print("\nPreorder traversal: ")
preorder(root)
print("\nPostorder traversal: ")
postorder(root)

