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
    def findMin(self):
        value=self
        while value.left is not None:
            value=value.left
        return value

    def delete(self,data):
        if data<self.data:
            if self.left:
                self.left=self.left.delete(data)
            else:
                print("Data not found")
        elif data>self.data:
            if self.right:
                self.right=self.right.delete(data)
            else:
                print("Data not found")
        else: 
            #when it has no child
            if self.left is None and self.right is None:
                print("\nDeleted data: ",self.data)
                return None
            elif self.left is None:
                print("\nDeleted right child is: ",self.data)
                return self.right
            elif self.right is None:
                print("\nDeleted left child is: ",self.data)
                return self.left
            else:
                #when it has two children
                a=self.right.findMin()
                print("\nDeleted items is ",self.data)
                self.data=a.data
                self.right=self.right.delete(a.data)
        return self


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

while True:

    if __name__=="__main__":
        root=Tree("s")
        nb=int(input("\nHow many elements would you like in your tree? "))
        for i in range(nb):
            item=input("What elements would you like to add? ")
            root.insert(item)
    while True:
        a=input("\nWhich function would you like to you use? Your options are: preorder, postorder, inorder, delete, exit. ")
        if a=="preorder":
            print("preorder traversal: ")
            preorder(root)
        elif a=="postorder":
            print("Postorder traversal: ")
            postorder(root)
        elif a=="inorder":
            print("Inorder traversal: ")
            inorder(root)
        elif a=="delete":
            b=input("Which element would you like to delete? ")
            root.delete(b)
        elif a=="exit":
            break
    break

    
