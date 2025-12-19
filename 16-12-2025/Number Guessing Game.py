# Fixed number that the user has to guess
secret_number = 7  

# To count how many attempts the user makes
attempts = 0  

# This loop will run until the correct number is guessed
while True:
    # Take input from the user
    guess = int(input("Guess the number: "))

    # Increase attempt count
    attempts += 1

    # Check if the guessed number is correct
    if guess == secret_number:
        print("Waoo It's Correct! You guessed the number.")
        print("Total attempts:", attempts)
        break      # Stop the loop when guessed correctly
    else:
        print("ohh! Wrong guess. Try again.")
