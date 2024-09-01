list=[]

nb=int(input("Number of elements in the list: "))

for i in range(nb):
    user_input=input("Enter the element: ")
    list.append(user_input)

for i in range(1,nb):
    key=list[i]
    j=i-1
    while key<list[j] and j>=0:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key

print("The sorted list is: ",list)