list=[]

nb=int(input("number of items: "))

for i in range(nb):
    user_input=input("Enter the element: " )
    list.append(user_input)

a=input("Enter the element that you want to find: ")

for i in range(len(list)):
    if list[i]==a:
        print(i)
