def merge_sort(list):
    if len(list)<=1:
        return list
    middle=len(list)//2
    half1=merge_sort(list[:middle])
    half2=merge_sort(list[middle:])
    return merge(half1,half2)

def merge(half1,half2):
    merge_list=[]
    i=j=0
    while i<len(half1) and j<len(half2):
        if half1[i]<half2[j]:
            merge_list.append(half1[i])
            i+=1
        else:
            merge_list.append(half2[j])
            j+=1

    merge_list.extend(half1[i:])
    merge_list.extend(half2[j:])
    return merge_list

#calling the function
list=[]

nb=int(input("Enter the number of elements in the list: "))

for i in range(nb):
    a=int(input("Enter the element: "))
    list.append(a)
a=merge_sort(list)
print("Sorted list",a)


