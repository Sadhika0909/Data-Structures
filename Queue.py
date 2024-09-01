class Queue:
    def __init__(self):
        self.queue=[]
    def empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def enqueue(self,item):
        self.queue.append(item)
        print("Enqueued item",item)
    def dequeue(self):
        if self.empty():
            return None
        else:
            return self.queue.pop(0)
    def front(self):
        if self.empty():
            return None
        else:
            return self.queue[0]
    def rear(self):
        if self.empty():
            return None
        else:
            return self.queue[-1]
    def display(self):
        return self.queue

queue1=Queue()
nb=int(input("Number of elements: "))

for i in range(nb):
    item=int(input("Item: "))
    queue1.enqueue(item)

#displaying the entire queue
print("The queue is ",queue1.display())

print("The front element is ",queue1.front())
print("The rear element is ",queue1.rear())

while not queue1.empty():
    print("Dequeued item",queue1.dequeue())

print("The queue is ",queue1.display())