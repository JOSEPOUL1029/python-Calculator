def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Error, cannot divide by zero"
    else:
        return a / b


def calculator_menu():
    while True:
        print("\n----CALCULATOR ------")
        print("1. Addition ( + )")
        print("2. Subtraction ( - )")
        print("3. Multiplication ( x )")
        print("4. Division ( / )")
        print("0. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "0":
            print("---Thank you for using calculator---!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == "1":
            print(f"Summation  of {a} and {b} = ", add(a, b))
        elif choice == "2":
            print(f"Substraction of {a} and {b} = ", sub(a, b))
        elif choice == "3":
            print(f"Multiplication of {a} and {b} = ", multiply(a, b))
        elif choice == "4":
            print(f"Division of {a} and {b} = ", div(a, b))


if __name__ == "__main__":
    calculator_menu()
