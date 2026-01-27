import random

# Function to return a random card from the deck
def deal_card():
    """Returns a random card from the deck."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 = Ace, 10 = Face cards
    return random.choice(deck)


# Function to calculate the score from a list of cards
def calculate_score(card_list):
    """Takes a list of cards and returns the total score."""
    
    # Blackjack condition: Ace + 10 = 21 with only 2 cards
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0   # 0 will represent Blackjack

    # If score is over 21 and Ace (11) is present, convert Ace to 1
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


# Function to compare user and computer scores and return the result
def compare_scores(user_score, computer_score):
    """Compares scores and decides the game result."""
    
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 🥳"
    elif user_score > computer_score:
        return "You win 😄"
    else:
        return "You lose 😤"


# Main function to run one round of Blackjack
def play_blackjack():
    
    logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

    # Lists to store cards
    player_cards = []
    dealer_cards = []

    # Initial scores
    player_score = -1
    dealer_score = -1

    # Flag to control game loop
    game_over = False

    # Deal two cards to both player and dealer
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # Main gameplay loop
    while not game_over:

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        # Display current game status
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        # Check if game should end
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True

        else:
            # Ask player if they want another card
            player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if player_choice == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    # Dealer draws cards until score is 17 or higher
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    # Final game results
    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))


# Loop to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_blackjack()
