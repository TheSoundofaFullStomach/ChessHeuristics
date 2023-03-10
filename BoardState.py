import chess
import numpy
import pandas
import learn as learn

# board state is an array of dimensions. Dimensions are boards squares and their respective threats/attacks
# each square of the board has:'
#   piece occupying square,
#   white pieces looking at it, white pieces that can be revealed to look at it next turn
#   black pieces looking at it, black pieces that can be revealed to look at it next turn
#   ex: b2 "wp,wb,,,"
board_state = []

def get_current_board_state(board):
    print(board_state)
    return board_state


def get_possible_board_states(board):
    board_states = [[]]
    print(board_states)
    return board_states


# returns three arrays:
#   one with squares that it can move to this turn,
#   one with squares that it can move to next turn,
#   one with squares that it can see if X-ray
def get_piece_scope(square):
    scope = [[], [], []]
    print(scope)
    return scope