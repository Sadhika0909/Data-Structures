a=0

def demo():
    global a
    a+=1
    print("hello",a)
    demo()
demo()