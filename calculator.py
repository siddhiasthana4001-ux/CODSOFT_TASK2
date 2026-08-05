def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def main():
    print("===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        symbol = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        symbol = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        symbol = '*'
    elif choice == '4':
        result = divide(num1, num2)
        symbol = '/'
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    print(f"\nResult: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()