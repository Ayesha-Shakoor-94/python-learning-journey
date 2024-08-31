import random

# Welcoming message
print('Welcome to Code_With_Ashu Number Guessing Game')

def guessgame()-> None:
    while True:
        # Generating a random number between 1 and 10
        random_number:int = random.randint(1, 10)
        
        # Asking the user to guess a number
        user_guess: int = int(input('Guess a number between 1 & 10: '))

         # Checking if the guessed number is out of range
        if user_guess < 1 or user_guess > 10:
            print('Error: Please enter a number between 1 and 10.')
            continue

        # Checking if the guessed number is correct
        if random_number != user_guess:
            print('Wrong Guess. Please try again...!')
        else:
            print("Congrats! Your guessed number is correct.")
            break

# Starting the game
guessgame()
