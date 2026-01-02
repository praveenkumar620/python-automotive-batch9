# Decorator definition
def calculator(func):
    def wrapper(a, b):
        print("Addition is:", a + b)
        return func(a, b)
    return wrapper


# Using the decorator
@calculator
def add(a, b):
    pass


# User input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

add(x, y)
