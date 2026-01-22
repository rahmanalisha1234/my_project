import random   # Importing the random module to generate random choices

# Lists containing all possible characters for the password
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Taking user input for how many characters they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# -------------------------------
# Sequential Password Generator
# (Letters → Symbols → Numbers)
# -------------------------------

password = ""   # Empty string to store the password

# Adding random letters
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

# Adding random symbols
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Adding random numbers
for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

# Printing the sequential password
print("Sequential password:", password)

# -----------------------------------
# Random Password Generator (Stronger)
# -----------------------------------

password_list = []   # List to store all characters before shuffling

# Adding random letters to the list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Adding random symbols to the list
for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Adding random numbers to the list
for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Printing the list before shuffling
print("Password list before shuffle:", password_list)

# Shuffling the list to randomize the order
random.shuffle(password_list)

# Printing the list after shuffling
print("Password list after shuffle:", password_list)

# Converting the list into a string
password = ""
for char in password_list:
    password += char

# Printing the final strong password
print(f"Your strong password is: {password}")
