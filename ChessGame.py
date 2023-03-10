import learn as Learn
import chess
import chess.polyglot
import chess.syzygy
import numpy
import pandas
import os
import random
from stockfish import Stockfish

import Board
import StockfishInterface
import HumanInterface
from OpponentInterface import OpponentInterface


# GLOBAL
board = []
opponent = 1
is_game_over = False
player_color = 1


def open_game():
    print("loading opening moves")

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


def end_game():
    print("loading end game tablebase")

    global board

    endgame_tablebase_path = "Syzygy_endgame_tablebases"
    endgame_tablebase = chess.syzygy.Tablebase.add_directory(endgame_tablebase_path)

# TODO
def choose_opponent():
    print("Who will I play?")

    global opponent

    # get opponent from interface

    opponent = OpponentInterface(opponent)

    return opponent


def init_chess_game():
    print("starting a new game")

    global board
    global opponent
    global player_color

    player_color = random.randint(1, 2)

    board = Board
    board.init_board()

    opponent = choose_opponent()

    opening_book = open_game()
    endgame_tablebase = end_game()


def start_open_chess_game():

    global is_game_over
    global board
    global opponent

    is_book_moves_remain = True

    if player_color == 1:
        print("I play as White")
    elif player_color == 2:
        print("I play as Black")
        opponent.get_move(board)

    while (not is_game_over) and (is_book_moves_remain):


        is_game_over = board.board_chess.is_game_over()
