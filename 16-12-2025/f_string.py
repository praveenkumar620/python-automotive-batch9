item_price = 19.99
item_count = 5
total_cost = item_price * item_count
print(f"Your total is ${total_cost:.2f} for {item_count} items.")
# Output: Your total is $99.95 for 5 items.

# You can also use the self-documenting
# expression specifier `=` for debugging
bugs = 'roaches'
count = 13
print(f"Debugging {bugs=} {count=}")
# Output: Debugging bugs='roaches' count=13

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)


name = "Praveen"
age = 23
price = 99.9567
number = 255

print("Name: %s" % name)          # String
print("Age: %d" % age)            # Integer
print("Price: %f" % price)        # Float
print("Price (2 decimal): %.2f" % price)   # Float with 2 digits
print("Hex lowercase: %x" % number)  # Hex (lowercase)
print("Hex uppercase: %X" % number)  # Hex (uppercase)
