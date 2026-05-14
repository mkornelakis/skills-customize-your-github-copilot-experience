
# 📘 Assignment: Games in Python (Hangman)

## 🎯 Objective

Build a text-based Hangman game using core Python concepts such as loops, conditionals, strings, lists, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Prepare the initial variables needed to run the game using the provided starter code.

#### Requirements
Completed program should:

- Randomly select one secret word from the provided `words` list.
- Create a structure to track guessed letters.
- Track the number of incorrect guesses.
- Define a maximum number of incorrect guesses allowed.

### 🛠️ Build the Main Game Loop

#### Description
Implement the interactive loop where the player guesses letters and receives feedback after each turn.

#### Requirements
Completed program should:

- Display the current word progress using underscores for unknown letters (for example: `_ _ t h _ n`).
- Prompt the player to enter one letter per turn.
- Update game state correctly for correct and incorrect guesses.
- Show the remaining number of incorrect guesses after each wrong attempt.
- End the loop when the word is fully guessed or the player runs out of attempts.

### 🛠️ Finish and Report Results

#### Description
Add clear end-of-game messages and verify that all game outcomes are handled.

#### Requirements
Completed program should:

- Display a congratulatory message when the player guesses the full word.
- Display a game-over message with the secret word when attempts are exhausted.
- Handle repeated guesses gracefully (without crashing).
- Use clear and student-friendly output messages throughout the game.
