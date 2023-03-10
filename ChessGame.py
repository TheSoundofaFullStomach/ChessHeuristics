import learn as Learn
import chess
import chess.polyglot
import numpy
import pandas
import os
import random
from stockfish import Stockfish

import Board


# GLOBAL
board = []
opponent = "stockfish"


def open_game():

    global board

    opening_books_path = "PolyGlot_opening_books"
    opening_books = os.listdir(opening_books_path)
    num_opening_books = len(opening_books)
    rand_idx = 0
    rand_opening_book = ""

    if num_opening_books > 0:
        rand_idx = random.randrange(0, num_opening_books)
        rand_opening_book = opening_books[rand_idx]

        opening_books_path = opening_books_path + "/" + rand_opening_book

        print(opening_books_path)
        # with chess.polyglot.open_reader(opening_books_path) as reader:
        #    for entry in reader.find_all(board.board_chess):
        #        print(entry.move, entry.weight, entry.learn)

        opening_memory = chess.polyglot.MemoryMappedReader(opening_books_path)

        #test
        # board.board_chess.push(chess.Move.from_uci("e2e4"))
        print(opening_memory.get(board.board_chess))

        return opening_memory


def init_chess_game():
    print("starting a new game")

    global board
    global opponent

    player_color = random.randint(1, 2)

    board = Board
    board.init_board()

    if opponent == "stockfish":
        opponent =

    opening_book = open_game()

    if player_color == 1:
        print("I play as White")
    elif player_color == 2:
        print("I play as Black")
