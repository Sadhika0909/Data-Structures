#Fibonacci function
def fibonacci(user_input):
    if user_input==1:
        return 0
    if user_input==2:
        return 1
    return fibonacci(user_input-2)+fibonacci(user_input-1)
user_input=int(input("Number of terms: "))
for i in range(1,user_input+1):
    print(fibonacci(i))