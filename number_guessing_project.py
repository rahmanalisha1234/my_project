import random
 
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
""" 
print(logo)

# Constants for number of attempts based on difficulty level
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


# Function to check the user's guess
def evaluate_guess(player_guess, correct_number, remaining_attempts):
    """
    Compares the player's guess with the correct number
    and returns the updated number of remaining attempts.
    """
    if player_guess > correct_number:
        print("Too High! Guess again.")
        return remaining_attempts - 1
    elif player_guess < correct_number:
        print("Too Low! Guess again.")
        return remaining_attempts - 1
    else:
        # Correct guess
        print(f"You got it! The correct answer was {correct_number}.")
        return remaining_attempts


# Function to set difficulty level
def choose_difficulty():
    """
    Asks the user to choose a difficulty level
    and returns the number of attempts allowed.
    """
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_choice == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


# Main game function
def start_game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    # Get the number of attempts based on difficulty
    attempts_left = choose_difficulty()

    # Initialize guess to a value that cannot be correct
    player_guess = None

    # Loop until the player guesses correctly or runs out of attempts
    while player_guess != target_number:

        print(f"You have {attempts_left} attempts remaining to guess the number.")

        # Take user input
        player_guess = int(input("Make a guess: "))

        # Evaluate the guess and update attempts
        attempts_left = evaluate_guess(player_guess, target_number, attempts_left)

        # If no attempts are left, end the game
        if attempts_left == 0:
            print(f"You've run out of guesses. You LOSE! . The random number chosen by the computer was {target_number}.")
            return
        


# Start the game
start_game()
