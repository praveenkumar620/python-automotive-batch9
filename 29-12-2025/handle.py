try:
    
    file = open("users.txt", "r")
    data = file.read()

    
    if data.strip() == "":
        print("The file is empty.")
    else:
        print("User Data:")
        print(data)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception:
    print("Error: File is corrupted or unreadable.")

finally:
    print("Program continues running smoothly.")
