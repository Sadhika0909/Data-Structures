list=[30,22,7,17,10,44,7,12,40,11]
a=len(list)

#Iterating through the entire list
for i in range(a):
    for j in range(0,a-i-1): #loop for swapping elements
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
#printing the sorted list
print("The sorted list is: ",list)