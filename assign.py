# num = int(input("Enter number: "))
# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
# print("Prime" if is_prime else "Not Prime")




# numbers = [5, 8, 2, 10, 3]
# print(("The Largest number is "),max(numbers))


# text = input("Enter text: ")
# vowels = 'aeiou'
# count = 0

# for ch in text.lower():
#     if ch in vowels:
#         count += 1

# print("Vowels:", count)

#  Write a Python program to print 'Hello World'.?

# print("Hello World")

# Write a Python program to take two numbers as input and print their sum.

# a=int(input("Enter 1st Number: "))
# b=int(input("Enter 2nd Number: "))
# print("The sum of these two numbers are: ",a+b)

#  Write a Python program to sort a list in ascending order.
# numbers = [5, 2, 9, 1, 7]

# numbers.sort()

# print("Sorted list:", numbers)

# Write a Python program to remove duplicates from a list. ?

# numbers = [2, 5, 3, 2, 8, 5, 3]
# numbers = list(set(numbers))
# print("List after removing duplicates:", numbers)

# Write a Python program to check if a string is a palindrome.

# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# Write a Python program to count the number of words in a sentence.

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Number of words:", len(words))

# Write a Python program to convert Celsius to Fahrenheit.
# c = float(input("Enter Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit =", f)

# Write a Python program to check if a character is a vowel or consonant.
# ch = input("Enter a character: ")

# if ch.lower() in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# Write a Python program to read a file and display its contents.
# file = open("Example.txt", "r")
# data = file.read()
# print(data)
# file.close()