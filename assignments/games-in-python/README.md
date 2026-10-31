# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input to practice core programming concepts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the variables and word-selection logic for a Hangman game before adding the gameplay loop.

#### Requirements
Completed program should:

- Define a list of possible words and randomly select one word for each round.
- Track guessed letters, incorrect guesses, and the maximum number of allowed mistakes.
- Display the hidden word as underscores or blanks that update as letters are guessed.
- Example:
  ```python
  word = "python"
  progress = "_ _ _ _ _ _"
  ```

### 🛠️ Play the Game

#### Description
Build the main game loop so the player can keep guessing letters until the word is solved or the game ends.

#### Requirements
Completed program should:

- Prompt the user to enter a letter guess.
- Check whether the letter is in the secret word and update the visible progress.
- Keep count of remaining attempts and show incorrect guesses.
- End the game when the player correctly guesses the full word or runs out of attempts.
- Print a clear win or lose message.
- Example:
  ```python
  Guess a letter: p
  Correct! Current progress: p _ _ _ _ _
  ```
