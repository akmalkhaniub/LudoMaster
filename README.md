# Ludo Game

A classic Ludo board game implemented in Python using Pygame.

## Overview

This Ludo game features:
- A classic 4-player board with red, blue, green, and yellow players
- Dice rolling mechanics with realistic animation
- Token movement according to standard Ludo rules
- Turn-based gameplay
- Win condition when all tokens reach the center

## Requirements

- Python 3.11 or higher
- Pygame 2.6.1 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ludo-game.git
   cd ludo-game
   ```

2. Install the required packages:
   ```
   pip install pygame
   ```

## How to Play

Run the game with:
```
python main.py
```

### Game Rules

- Each player has 4 tokens
- Roll a 6 to move a token out of the home area
- Move tokens clockwise around the board according to dice rolls
- Reach the center with all 4 tokens to win
- Take turns rolling the dice and moving tokens

## Project Structure

- `main.py`: Main game loop and initialization
- `game/constants.py`: Game constants and configuration
- `game/board.py`: Game board representation and rendering
- `game/dice.py`: Dice rolling mechanics
- `game/player.py`: Player management
- `game/token.py`: Token movement and mechanics
- `assets/`: Game assets

## License

This project is open source and available under the MIT License.
