# 🎮 Hangman Game

A simple text-based **Hangman** game built in **Python** where the player guesses a hidden word one letter at a time before running out of attempts.

This project demonstrates the use of fundamental Python programming concepts such as loops, conditional statements, functions, lists, string manipulation, randomization, and input validation.

---

## 📌 Features

- 🎲 Randomly selects a word from a predefined list.
- 🔤 Guess one letter at a time.
- ❤️ Allows up to **6 incorrect guesses**.
- 🎨 Displays Hangman ASCII art after each wrong guess.
- ✅ Prevents duplicate letter guesses.
- ⚠️ Validates user input.
  - Only accepts a single alphabetic character.
- 📝 Displays
  - Current word progress
  - Previously guessed letters
  - Remaining incorrect guesses
- 🔄 Supports playing multiple rounds.
- 🎯 Ensures the same word is **not selected in two consecutive games**.

---

## 🛠 Technologies Used

- Python 3
- random module

---

## 💻 Sample Gameplay

```text

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        Welcome to Hangman Game!

Guess the word. You have 6 incorrect guesses allowed.
You have to guess one letter at a time.
Only lowercase letters are used.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

       ------
       |    |
       |
       |
       |
       |
    --------

Word: _ _ _ _ _ _
Incorrect guesses left: 6

Guess a letter: y
Good guess!
y is in the word.


       ------
       |    |
       |
       |
       |
       |
    --------
 
Word: _ _ y _ _ _
Incorrect guesses left: 6
Guessed letters: y

Guess a letter: z
Sorry, z is not in the word.


       ------
       |    |
       |    O
       |
       |
       |
    --------

Word: _ _ y _ _ _
Incorrect guesses left: 5
Guessed letters: y, z

...

Congratulations! You guessed the word: rhythm

```

---

## 💻 Code Overview

| Function | Purpose |
|---|---|
| `choose_word(word_list)` | Randomly selects a word, avoiding repeating the previous round's word |
| `display_progress(word, guessed_letters)` | Builds the current display string (letters + blanks) |
| `is_word_guessed(word, guessed_letters)` | Checks if the full word has been guessed |
| `play_hangman()` | Runs a single round of the game |
| `main()` | Handles the play-again loop |

---

## 📚 Key Concepts Used

- `random` module (`random.choice`) for word selection
- `while` loops, including a `while...else` construct to detect a loss
- `if` / `elif` / `else` conditionals for game logic and input validation
- String methods (`.lower()`, `.strip()`, `.isalpha()`, `.join()`)
- Lists (`WORDS` list, `guessed_letters` list, `HANGMAN_STAGES` list)

---

## 📝 Customization

- **Add more words:** edit the `WORDS` list.
- **Change difficulty:** adjust `MAX_INCORRECT_GUESSES`.
- **Change the drawing:** edit the ASCII art strings in `HANGMAN_STAGES`.

---

## 🚀 Future Improvements

- Load words from an external dictionary file.
- Add multiple difficulty levels.
- Categorize words (Animals, Countries, Technology, etc.).
- Track player score across multiple games.
- Add hints for difficult words.
- Display guessed and remaining alphabets.
- Create a graphical version using Tkinter or Pygame.

---

## 🎯 Project Objective

This project was developed as part of the **CodeAlpha Python Programming Internship** to demonstrate a text-based Hangman game using core Python programming concepts and problem-solving techniques.

---

## 👨‍💻 Author

**Gaurav Kumar Ojha**
