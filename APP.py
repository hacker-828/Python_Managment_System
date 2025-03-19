from package import operation

print("Hello")
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

print("What Dod U Wanna Do Today:\n\
    1. Addition\n\
    2. Multiplication\
")

operations = input("ENTER THE OPERATION YOU WILL LIKE TO USE: ")

if len(operations) == 0:
    print("Enter a valid operation")
else:
    addition = "1"
    multiply = "2"

    operations = operations.lower()
    if operations == addition :
        result = operation.add(num1,num2)
        print(result)

    elif operations == multiply:      
        result = operation.multi(num1,num2)
        print(result)
