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


# GLOBAL

board = Board
chess_game = ChessGame

def print_start():
    # Use a breakpoint in the code line below to debug your script.
    print("Starting Chess Heuristics")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def run_chess():

    global chess_game

    print_start()
    chess_game = ChessGame
    ChessGame.init_chess_game()

    stockfish = Stockfish

if __name__ == '__main__':
    run_chess()
