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

inorder(root)
