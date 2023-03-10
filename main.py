import learn as Learn
import chess
import chess.polyglot
import numpy
import pandas
import os
import random
from stockfish import Stockfish

import Board
import ChessGame

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#MAIN.PY

board = Board

def print_start():
    # Use a breakpoint in the code line below to debug your script.
    print("Starting Chess Heuristics")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def run_chess():

    global board

    board = Board
    player_color = random.randint(1, 2)


    print_start()
    Board.init_board()

    stockfish = Stockfish

    if player_color == 2:
        print("let stockfish go first")


if __name__ == '__main__':
    run_chess()
