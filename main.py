from app.calculator import add, subtract, multiply, divide, square

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")

    choice = input("Choose operation (1-5): ")

    if choice == "5":
        a = float(input("Enter a number: "))
        print("Result:", square(a))
    elif choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()