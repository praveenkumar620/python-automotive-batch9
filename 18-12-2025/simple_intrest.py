# Import Calculator program
from calculator import add, multiplication, division

# Simple Interest calculation using calculator functions
def simple_interest(p, r, t):
    pr = multiplication(p, r)
    prt = multiplication(pr, t)
    si = division(prt, 100)
    return si

# Input from user
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time: "))

# Function call
result = simple_interest(principal, rate, time)

# Output
print("Simple Interest is:", result)
