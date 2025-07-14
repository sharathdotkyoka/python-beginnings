import math

while True:
    operation = input("choose the operation +,-,*,/,%,sqrt or q to quit:" )
    
    if operation == "q":
        print("calculator closed")
        break
    
    if operation == "sqrt":
        num = int(input("enter the number: "))
        if num < 0:
            print("cannot square root a negative number")
        else:
            print(math.sqrt(num))
        continue
    try:
        num1 = int(input("input the first number: "))
        num2 = int(input("input the second number: "))
    except ValueError:
        print("invalid input, please enter digits only.")
        continue
    
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("cannot be divided by zero")
        else:
            print(num1 / num2)
    elif operation == "%":
        print((num1 / num2) * 100)
    else:
        print("invalid operation")