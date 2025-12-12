file = open("Example.txt", "r")   # r = read mode
content = file.read()
print(content)
file.close()

file = open("Example.txt", "w")   # w = write mode
file.write("This is new text.")
file.close()
