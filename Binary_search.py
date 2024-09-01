a=[2,4,5,6,10,13,14,15,20,22]

user=int(input("What is the target element? "))
b=0
e=len(a)-1
result=0

while b<=e:
    m=b+(e-b)//2
    if user==a[m]:
        result=m
        break
    elif user<a[m]:
        e=m-1
    else:
        b=m+1
#printing the result
if result!=0:
    print("The element was found in the following index: ",m)
else:
    print("The element was not found")