logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Function to find and print the highest bidder

def find_highest_bidder(bid_data):
    highest_bid = 0
    winner_name = ""

    # Loop through all bidders in the dictionary
    for name in bid_data:
        bid_amount = bid_data[name]

        # Check if current bid is higher than the highest bid so far
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = name

    # Print the winner and the highest bid
    print(f"\nThe winner is {winner_name} with a bid of ${highest_bid} 🎉")


# Dictionary to store bids in the form {name: price}
all_bids = {}

# Variable to control the bidding loop
is_bidding = True

# Main bidding loop
while is_bidding:

    # Ask user for name and bid amount
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $ "))

    # Store the bid in the dictionary
    all_bids[user_name] = user_bid

    # Ask if there are more bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # If no more bidders, stop and find the winner
    if more_bidders == "no":
        is_bidding = False
        find_highest_bidder(all_bids)

    # If more bidders, clear the screen (just prints blank lines)
    elif more_bidders == "yes":
        print("\n" * 20)
