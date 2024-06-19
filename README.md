# 2048

## Overview

The goal of this project is to model an AI player for the 2048 game. The AI is designed as a max player, while the computer acts as a chance player by placing a random 2-tile on the board. The AI uses a depth-3 game tree and the expectimax algorithm to make decisions. The evaluation function at the leaf nodes of the game tree is based on the score returned by the game engine.

## Key Components

1. Game Tree Structure:

* Root Level: Player
* Level 1: Computer
* Level 2: Player
* Level 3: Terminal with payoff (the leaf nodes represent the evaluation of the game state)

This tree represents all the game states of a player-computer-player sequence (the player makes a move, the computer places a tile, and then the player makes another move, and then evaluates the score) from the current state. Compute the expectimax values of all the nodes in the game tree and return the optimal move for the player.

2. Game Interaction:

* Play the game manually using arrow keys.
* Press 'Enter' to let the AI play and 'Enter' again to stop the AI.
* The game engine code in game.py manages the game state and score evaluation.

The AI aims to maximize the player's score by making optimal moves based on the expectimax values computed from the game tree. The AI should frequently reach the 512 tile and score over 5000.

## Usage

To run the program, use the following command:
```
python main.py
```
To test the AI's performance on 15 test states, use:
```
python main.py -t 1
```

## In-Game Keyboard Options

* 'r': Restart the game
* 'u': Undo a move
* '3'-'7': Change board size
* 'g': Toggle grayscale
