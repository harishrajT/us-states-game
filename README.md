# U.S. States Game

This is an interactive U.S. States guessing game built using Python's Turtle graphics and Pandas libraries. The goal of the game is to correctly guess the names of all 50 U.S. states.

## Features

- **Interactive Input:** The user is prompted to input the name of a U.S. state.
- **Real-time Display:** When the user guesses a state correctly, it is displayed on the map at its corresponding location.
- **Progress Tracker:** The game tracks the number of correct guesses out of 50.
- **Exit Option:** The user can type "Exit" to stop the game and receive a CSV file listing the states they missed.
- **Learning Assistance:** The game generates a file `States_to_Learn.csv` containing the states that were not guessed during the session, helping users study the ones they missed.

## Requirements

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)
- Pandas library (`pip install pandas`)

## How to Play

1. **Clone the repository** or download the code files.
2. Ensure that the following files are in the same directory:
   - `50_states.csv` (a CSV file containing U.S. states and their coordinates)
   - `blank_states_img.gif` (a blank U.S. map image file used as the background)
3. Run the `us_states_game.py` script.
   - The game will display a blank map of the U.S.
   - Enter the name of a state in the text box when prompted.
   - Correctly guessed states will appear on the map at their respective locations.
   - If you want to end the game, type "Exit". A `States_to_Learn.csv` file will be created with the names of the states you missed.
   
