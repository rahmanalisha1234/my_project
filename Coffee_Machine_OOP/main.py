# -------------------- IMPORT REQUIRED CLASSES --------------------
# Menu         -> Handles available drinks and their details
# CoffeeMaker  -> Manages resources (water, milk, coffee)
# MoneyMachine -> Handles coin processing and payments

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# -------------------- CREATE OBJECTS --------------------
# Creating objects (instances) of each class

money_machine = MoneyMachine()     # Object to manage money transactions
coffee_maker = CoffeeMaker()       # Object to manage coffee resources
menu = Menu()                      # Object to manage menu items


# -------------------- MACHINE STATE --------------------
# This variable controls whether the machine is ON or OFF

is_on = True


# -------------------- MAIN LOOP --------------------
# The coffee machine will keep running until the user turns it off

while is_on:

    # Get all available drink options as a string (e.g., "espresso/latte/cappuccino")
    options = menu.get_items()

    # Ask the user to choose a drink
    choice = input(f"What would you like? ({options}): ")

    # Turn off the coffee machine
    if choice == "off":
        is_on = False

    # Print current resource and money report
    elif choice == "report":
        coffee_maker.report()      # Shows remaining water, milk, coffee
        money_machine.report()     # Shows total money earned

    # Process drink order
    else:
        # Find the drink object selected by the user
        drink = menu.find_drink(choice)

        # Step 1: Check if enough resources are available
        # Step 2: Check if payment is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Step 3: Make the coffee if all conditions are satisfied
            coffee_maker.make_coffee(drink)
