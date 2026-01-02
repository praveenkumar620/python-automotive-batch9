# Decorator definition
def calculator(func):
    def wrapper(a, b, choice):
        if choice == 1:
            print("Addition is:", a + b)
        elif choice == 2:
            print("Subtraction is:", a - b)
        elif choice == 3:
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Division is:", a / b)
        else:
            print("Invalid choice")
        return func(a, b, choice)
    return wrapper


# Using the decorator
@calculator
def calculate(a, b, choice):
    pass


# User input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Divide")

ch = int(input("Enter your choice: "))

calculate(x, y, ch)
