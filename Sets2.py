students=set([])
print(students)

nb=int(input("Number of students: "))

for i in range(nb):
    s=input("Student: ")
    students.add(s)

while True:
        f=input("\nWhich function would you like to you use? Your options are: add, remove, display, search, total, clear, exit. ")
        if f=="add":
            a=input("Which student's name would you like to add? ")
            students.add(a)
        elif f=="remove":
            r=input("Which student's name would you like to remove? ")
            students.remove(r)
        elif f=="display":
            print("Students: ",students)
        elif f=="search":
            c=input("Which student's name would you like to check? ")
            if c in students:
                print("The student is present.")
            else:
                print("The student is absent.")
        elif f=="total":
            print(len(students))
        elif f=="clear":
            students.clear()
            print("Students:",students)
        elif f=="exit":
            break

    


