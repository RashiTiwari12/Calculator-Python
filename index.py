def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


while True:
    print("Select Operation(Choose 1 or 2 or 3 or 4) :")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:: "))

        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(sub(num1, num2))
        elif choice == '3':
            print(multi(num1, num2))
        elif choice == '4':
            print(div(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid choice")
