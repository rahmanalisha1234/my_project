import random

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 
             'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 
             'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 
             'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 
             'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 
             'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 
             'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess',
             'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 
             'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 
             'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 
             'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify',
             'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
             'onyx', 'ovary', 'oxidize', 'oxygen', 
             'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 
             'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum',
             'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
             'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome',
             'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths',
             'unknown', 'unworthy', 'unzip', 'uptown',
             'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism',
             'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


# Print the Hangman logo at the start of the game
print(logo)

# Total number of lives the player has
lives = 6

# Choose a random word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # (For testing only – remove in real game)

# Create a placeholder string like "_ _ _ _"
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)

# Game control variables
game_over = False
correct_letters = []

# Main game loop
while not game_over:

    # Show how many lives are left
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed this letter
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")

    display = ""

    # Build the display word based on guesses so far
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the guessed letter is not in the chosen word, reduce a life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        # If no lives are left, end the game and show the correct word
        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS '{chosen_word}'! YOU LOSE **********************")

    # If there are no blanks left, the user has won
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # Print the current stage of the hangman based on remaining lives
    print(stages[lives])
