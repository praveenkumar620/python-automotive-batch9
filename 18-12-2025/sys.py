# Using the sys module, write a program that redirects output of a program to a text file.

# Import sys module
import sys

# Open a text file in write mode
file = open("output.txt", "w")

# Redirect standard output to the file
sys.stdout = file

# Print statements (output will go into the file)
print("This output is redirected to a text file.")
print("Python makes file handling easy.")
print("This line will not appear on the screen.")

# Close the file
file.close()
