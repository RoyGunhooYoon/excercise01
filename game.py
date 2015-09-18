#! /usr/bin/python3

"""My TeamTreeHouse python challenge: dungeon game"""

import game_core, game_grid

# Rules: Player has to reach the door without getting caught by a monster.
#        Player and Monster can move 1 cell each turn in any direction.
#        Attempt to move outside the grid is not allowed
#        Player, Monster and Door cannot be at the same starting location.

# Grid: list of (x,y) tuple co-ordinate
#       width: 3, height: 3

# Game pieces: player, monster, door

# Setting game: unique random starting location for each pieces

# Moves: Player: decides where to move
#        Monster: moves randomly
#        Door: does not move.

width = 3
height = 3

grid = game_grid.make_grid(width, height)

#Data structure: {type:{trace:[]}}
pieces = {
    'player': {'trace': []},
    'monster': {'trace': []},
    'door': {'trace': []}
    }

dirs = {
    'n': (0, -1),
    'ne': (1, -1),
    'e': (1, 0),
    'se': (1, 1),
    's': (0, 1),
    'sw': (-1, 1),
    'w': (-1, 0),
    'nw': (-1, -1)
}

#Start the game
game_core.start_game(pieces, dirs, grid)
