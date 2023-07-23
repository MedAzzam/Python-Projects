import random

def guess_number():
    number = random.randint(1, 10)
    chances = 3

    while chances > 0:
        # Hundle the User input
        try:
            guess: int = int(input("Guess the number (between 1 and 10): "))
        except ValueError as e :
            print("Please enter a valid number.")
        
        # Check if the guess is correct
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")
            return
    # If the player couldn't guess the number within the allowed chances    
    print(f"Game over. The number was {number}")

guess_number()