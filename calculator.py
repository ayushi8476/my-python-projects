def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1/2/3/4): "))
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Zero is not divisible.")
    else:
        print("Invalid choice!")

calculator()
