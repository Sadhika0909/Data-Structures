list=[]

nb=int(input("Enter the number of elements in the list: "))

for i in range(nb):
    a=int(input("What is the element: "))
    list.append(a)

for i in range(1,nb):
    key=list[i]
    j=i-1
    #Moving greater element to one position ahead
    while j>=0 and key<list[j]:
        list[j+1]=list[j]
        j-=1
    list[j+1]=key

print("The sorted list is: ",list)