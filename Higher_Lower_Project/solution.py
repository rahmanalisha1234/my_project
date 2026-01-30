import random
from art import logo, vs
from game_data import data


# -------------------- Helper Functions --------------------

def format_account(account):
    """
    Takes account data (dictionary) and
    returns a nicely formatted string for display.
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def is_guess_correct(user_choice, followers_a, followers_b):
    """
    Compares follower counts and checks
    whether the user's guess is correct.
    """
    if followers_a > followers_b:
        return user_choice == "a"
    else:
        return user_choice == "b"


# -------------------- Game Starts --------------------

print(logo)

score = 0                    # Keeps track of user's score
game_running = True          # Controls the game loop

# Pick an initial random account for comparison
account_b = random.choice(data)

while game_running:

    # Move previous B account to A
    account_a = account_b
    account_b = random.choice(data)

    # Ensure both accounts are not the same
    if account_a == account_b:
        account_b = random.choice(data)

    # Display the two accounts
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    # Ask user for their guess
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen and show logo again
    print("\n" * 20)
    print(logo)

    # Get follower counts
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    # Check if user's guess is correct
    correct = is_guess_correct(user_choice, followers_a, followers_b)

    if correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_running = False
