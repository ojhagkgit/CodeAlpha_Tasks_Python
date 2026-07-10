# Hangman Game

A simple text-based Hangman game built in Python, where the player guesses a
secret word one letter at a time before running out of incorrect guesses.

## Features

- 5 predefined words to choose from (no external file or API required)
- Random word selection each round, avoiding an immediate repeat of the
  previous round's word
- 6 incorrect guesses allowed before the game ends
- ASCII-art hangman drawing that updates with each wrong guess
- Input validation (rejects empty input, multiple characters, non-letters,
  and repeated guesses)
- Tracks and displays previously guessed letters
- "Play again" loop so you can keep playing without restarting the script

## Requirements

- Python 3.6 or later (uses f-strings)
- No external libraries — only the built-in `random` module

## How to Run

```bash
python3 CodeAlpha_Hangman.py
```

## How to Play

1. When the game starts, a random word is chosen from the word list.
2. The word is displayed as a row of blanks (`_`), one per letter.
3. Enter one letter at a time when prompted.
   - If the letter is in the word, it's revealed in its correct position(s).
   - If the letter is not in the word, you lose one guess and the hangman
     drawing progresses.
4. The game ends when either:
   - You guess every letter in the word (**you win**), or
   - You reach 6 incorrect guesses (**you lose**, and the word is revealed).
5. After each round, you'll be asked if you want to play again (`y`/`n`).

## Project Structure

```
CodeAlpha_Hangman.py   # Main game script
README.md              # This file
```

## Code Overview

| Function | Purpose |
|---|---|
| `choose_word(word_list)` | Randomly selects a word, avoiding repeating the previous round's word |
| `display_progress(word, guessed_letters)` | Builds the current display string (letters + blanks) |
| `is_word_guessed(word, guessed_letters)` | Checks if the full word has been guessed |
| `play_hangman()` | Runs a single round of the game |
| `main()` | Handles the play-again loop |

## Key Concepts Used

- `random` module (`random.choice`) for word selection
- `while` loops, including a `while...else` construct to detect a loss
- `if` / `elif` / `else` conditionals for game logic and input validation
- String methods (`.lower()`, `.strip()`, `.isalpha()`, `.join()`)
- Lists (word list, guessed-letters list, hangman stage list)

## Customization

- **Add more words:** edit the `WORDS` list.
- **Change difficulty:** adjust `MAX_INCORRECT_GUESSES`.
- **Change the drawing:** edit the ASCII art strings in `HANGMAN_STAGES`.
