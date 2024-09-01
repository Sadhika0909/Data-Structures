list=[]

nb=int(input("Enter the number of elements"))

for i in range(nb):
    user_input=input("what element do you want in your list? ")
    list.append(user_input)

user=input("What item do you want to search for? ")
beginning=0
end=nb-1
result=-1

while beginning<=end:
    middle=(beginning+end)//2
    if list[middle]==user:
        result=middle
        print(result)
        break
    elif user>list[middle]:
        beginning=middle+1
    else:
        end=middle-1
if result!=-1:
    print("The element is found at the index ",middle)
else:
    print("Element was not found.")
        