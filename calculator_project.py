logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# ---------- Operations to perform ----------

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract second number from first
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide first number by second
def divide(n1, n2):
    return n1 / n2


# Dictionary that links operation symbols to their functions
operation_to_perform = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Example of using the dictionary to call a function
# print(operation_to_perform["*"](4, 8))   # Output: 32


# ---------- Calculator Program ----------

def calculator():

    # Variable to control whether the calculator should keep running
    should_continue = True

    # Ask the user for the first number
    num1 = float(input("What's the first number?: "))

    # Keep looping until the user decides to stop
    while should_continue:

        # Print all available operation symbols (+, -, *, /)
        for symbol in operation_to_perform:
            print(symbol)

        # Ask the user to choose an operation
        operation_symbol = input("Pick an operation: ")

        # Ask the user for the next number
        num2 = float(input("What is the next number?: "))

        # Get the correct function from the dictionary and call it
        answer = operation_to_perform[operation_symbol](num1, num2)

        # Print the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue with the current result
        choice_of_user = input(
            f"Type 'y' to continue calculating with {answer}, "
            f"or type 'n' to start a new calculation: "
        )

        # If user chooses 'y', use the answer as the next first number
        if choice_of_user == 'y':
            num1 = answer

        # If user chooses 'n', stop this loop and restart the calculator
        else:
            should_continue = False
            print("\n" * 20)   # Print blank lines to clear the screen
            calculator()      # Restart the calculator by calling the function again


# ---------- Start the Calculator ----------
calculator()
