class Stack:
    def __init__(self,nb): #constructor
        self.stack=[]
        self.nb=nb
    def push(self,a):
        if len(self.stack)<self.nb:
            self.stack.append(a)
        else:
            print("Stack is full")
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty")
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")
    def isEmpty(self):
        return len(self.stack)==0
    def isFull(self,nb):
        return len(self.stack)>nb
    
#if __name__=="__main__":
s=int(input("What is the number of elements? "))
stack1=Stack(s)
#b=stack1.isEmpty
#print(b)
stack1.push(2)
stack1.push(31)
stack1.push(17)
stack1.push(3)
print("Stack after operations",stack1.stack)

print("Popped element is",stack1.pop())
print("Stack after operations",stack1.stack)

print("Top element is",stack1.peek())
print("Is the stack full?", stack1.isFull(s))