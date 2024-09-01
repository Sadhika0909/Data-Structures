list=[15,58,95,23,75,48,65,97,11,2,6]

user_input=int(input("What is your number?"))

for i in range(len(list)):
    if user_input==list[i]:
        print(i)
