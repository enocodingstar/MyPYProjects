while True:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input")
    else:
        try:
            num2 = float(input("Enter the second number :"))
        except ValueError:
            print("Invalid input")
        else:
            try:
                operator = input("Enter an operator: ")
            except ValueError:
                print("Invalid input")
            else:
                if (operator == "add"):
                    print(num1 + num2)
                elif (operator == "subtract"):
                    print(num1 - num2)
                elif (operator == "multiply"):
                    print(num1 * num2)
                elif (operator == "divide"):
                    try:
                        quotient = num1 / num2
                    except ZeroDivisionError:
                        print("Zero division error")
                    else:
                        print(quotient)
                else: 
                    print("invalid operator")
    try:
        answer = input("Would you like to continue? ").strip().lower()
    except ValueError:
        print("Invalid input")
    else:
        if (answer == "no"):
            print("Thank you for using the calculator")
            break
