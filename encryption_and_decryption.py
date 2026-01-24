logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# List of lowercase alphabets used for shifting letters
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Caesar cipher function to encode or decode a message
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If the user chooses decode, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each character in the input text
    for letter in original_text:

        # If the character is not in the alphabet (space, number, symbol),
        # keep it unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the new position after shifting the letter
            shifted_position = alphabet.index(letter) + shift_amount

            # Wrap around if the position goes beyond 'z' or before 'a'
            shifted_position %= len(alphabet)

            # Add the shifted letter to the output text
            output_text += alphabet[shifted_position]

    # Print the final encoded or decoded result
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Control variable to restart the cipher program
should_continue = True

# Main program loop
while should_continue:

    # Ask the user whether to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Ask the user for the message
    text = input("Type your message:\n").lower()

    # Ask the user for the shift number
    shift = int(input("Type the shift number:\n"))

    # Normalize large shift values to stay within alphabet range
    shift = shift % len(alphabet)

    # Call the Caesar cipher function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("GoodBye")
