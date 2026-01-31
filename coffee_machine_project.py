# -------------------- MENU DATA --------------------
# Stores details of each coffee:
# - ingredients required
# - cost of the drink

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# -------------------- MACHINE STATUS --------------------

# Stores total money earned by the coffee machine
profit = 0

# Stores available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# -------------------- FUNCTIONS --------------------

def is_resource_sufficient(order_ingredients):
    """
    Checks whether the machine has enough ingredients
    to prepare the selected drink.

    Returns:
    True  -> if all ingredients are sufficient
    False -> if any ingredient is insufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Takes coin input from the user and
    calculates the total amount inserted.
    """
    print("Please insert coins.")

    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def is_transaction_successful(money_received, cost_of_drink):
    """
    Checks if the user has inserted enough money.

    Returns:
    True  -> if payment is sufficient
    False -> if payment is insufficient
    """
    global profit

    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from resources
    and serves the coffee.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕ Enjoy!!")

# -------------------- MAIN PROGRAM --------------------

# Controls whether the coffee machine is running
is_on = True

while is_on:

    # Ask user for their choice
    choice_of_user = input(
        "What would you like? (espresso/latte/cappuccino): "
    )

    # Turn off the machine
    if choice_of_user == "off":
        is_on = False

    # Print current resource report
    elif choice_of_user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    # Handle drink order
    else:
        drink = MENU[choice_of_user]

        # Step 1: Check resources
        if is_resource_sufficient(drink["ingredients"]):

            # Step 2: Process payment
            payment = process_coins()

            # Step 3: Check transaction and make coffee
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice_of_user, drink["ingredients"])
