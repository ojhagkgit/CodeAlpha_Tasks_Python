"""
Hangman Game
A simple text-based Hangman game where the player guesses a word by one letter at a time.

Key concepts used: random, while-else loop, if-else, strings, lists.
"""

import random

# Predefined list of 5 words (no file or API needed).
WORDS = ["rhythm", "youtube", "quantum", "immutable", "polymorphism"]

MAX_INCORRECT_GUESSES = 6

# Helped by ChatGPT for HANGMAN_STAGES
HANGMAN_STAGES = [

    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,

    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]
# The right hand and right leg uses "\\" instead of "\".
# The first "\" escapes, the second one tells Python 
# "I want an actual backslash character here, not the start of an escape sequence like \n or \t."

# Make sure that word guessed in current game isn't same as
# the word guessed in the very last game in a single run of the program
last_word = None

def choose_word(word_list):
    """Pick a random word, not the last one, from the given list."""

    global last_word
    word = random.choice(word_list)
    while word == last_word and len(word_list) > 1:
        word = random.choice(word_list)
    last_word = word
    return word;


def display_progress(word, guessed_letters):
    """Return a string showing guessed letters and blanks for the rest."""

    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip();


def is_word_guessed(word, guessed_letters):
    """Check whether every letter in the word has been guessed."""

    for letter in word:
        if letter not in guessed_letters:
            return False;
    return True;


def play_hangman():

    word = choose_word(WORDS)
    guessed_letters = []        # letters that the player has already tried
    incorrect_guesses = 0

    print('\n')
    print("+" * 60)
    print("\n\t\tWelcome to Hangman Game!\n")
    print("Guess the word. You have "f"{MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("You have to guess one letter at a time.")
    print("Only lowercase letters are used.")
    print("+" * 60)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:

        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_progress(word, guessed_letters))
        print("Incorrect guesses left: "f"{MAX_INCORRECT_GUESSES - incorrect_guesses}")

        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = input("\nGuess a letter: ").lower().strip()

        # --- Input validation ---
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue;

        if guess in guessed_letters:
            print("You already guessed "f"{guess}. \nTry a different letter.\n")
            continue;

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess! \n"f"{guess} is in the word.\n")

            if is_word_guessed(word, guessed_letters):
                print("\nCongratulations! You guessed the word: "f"{word}")
                break;
        else:
            incorrect_guesses += 1
            print("Sorry, "f"{guess} is not in the word.\n");
    
    else:
        # while-else runs only if the loop ended without 'break'
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Game over! You've run out of guesses.")
        print("The word was: "f"{word}");


def main():

    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("\nThanks for playing Hangman! Goodbye.\n");


if __name__ == "__main__":
    main();
