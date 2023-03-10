import learn as learn
import chess
import numpy
import pandas
import chess
import BoardState

# GLOBAL

# board: board[rank][file] [row][col]
# moves: "[player][piecetype][currentlocation][destination]" "bbb1a2" -> black bishop from b1 to a2
# players: white = "w", black "b"
# pieces: pawn = "p", rook = "r", bishop = "b", knight = "n", queen = "q", king = you "k"

board = [[]]
board_FEN = ""
board_chess = chess.Board() # the board object provided by the library
board_state = [[], []]
is_whitetomove = True
is_blacktomove = False


# TODO
def init_board():
    print("Initializing board")
    global board
    global board_FEN
    global board_chess
    global board_state
    global is_whitetomove
    global is_blacktomove

    board = board = [["  "]*9 for i in range(9)]
    board_chess = chess.Board()
    board_FEN = board_chess.fen()
    print(board)

def reset_board():
    global board
    board = chess.Board()
    print(board)


# done
def convert_file_idx_to_file_letter(file_idx):
    file = "x"

    if file_idx == 1:
        file = "a"
    elif file_idx == 2:
        file = "b"
    elif file_idx == 3:
        file = "c"
    elif file_idx == 4:
        file = "d"
    elif file_idx == 5:
        file = "e"
    elif file_idx == 6:
        file = "f"
    elif file_idx == 7:
        file = "g"
    elif file_idx == 8:
        file = "h"

    return file


# done
def convert_file_letter_to_file_idx(file_letter):

    file = -1

    if file_letter == "a":
        file = 1
    elif file_letter == "b":
        file = 2
    elif file_letter == "c":
        file = 3
    elif file_letter == "d":
        file = 4
    elif file_letter == "e":
        file = 5
    elif file_letter == "f":
        file = 6
    elif file_letter == "g":
        file = 7
    elif file_letter == "h":
        file = 8

    return file


# done
def convert_square_to_arr_idx(square):

    idx = []
    file_idx = convert_file_letter_to_file_idx(square[0])
    rank_idx = int(square[1])
    idx.append(rank_idx)
    idx.append(file_idx)

    return idx


# done
def convert_arr_idx_to_square(idx):

    square = ""
    file = convert_file_idx_to_file_letter(idx[1])
    rank = idx[0]
    square = square + file + rank

    return square


# TODO
def convert_FEN_to_board():
    print("board")

# TODO later
def find_existing_pieces(piece_type, player):
    print("temp")


# TODO
def is_legal_move(move):
    print("temp")



# TODO
def get_turn_move(move):
    print("temp")


# TODO
def calc_board_state():

    global board
    return BoardState.get_current_board_state(board), BoardState.get_possible_board_states(board)


# TODO
def print_board():
    print("temp")
