while True:
    num1 = float(input("Enter the first number: "))
    num2 = ""
    operator = ""
    
    if (num1 / 1 == num1):
        num2 = float(input("Enter the second number: "))
    else:
        print("Invalid input")
    if (num2 / 1 == num2):
        operator = input("Enter an operator: ")
    else:
        print("Invalid input")

    
    if (operator == "add"):
        print(num1 + num2)
    elif (operator == "subtract"):
        print(num1 - num2)
    elif (operator == "multiply"):
        print(num1 * num2)
    elif (operator == "divide"):
        print (num1 / num2)
    else: 
        print("invalid opeartor")
    
    answer = input("Would you like to continue? ").strip().lower()
    if (answer == "no"):
        print("Thank you for using the calculator")
        break
