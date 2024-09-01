list=[]

nb=int(input("Enter the number of elements in the list: "))

for i in range(nb):
    user_input=input("what element do you want in your list? ")
    list.append(user_input)

for i in range(nb):
    for j in range(0,nb-i-1): 
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print("The sorted list is: ",list)