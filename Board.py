import learn as learn
import chess
import numpy
import pandas
import chess
import BoardState

# board: board[rank][file] [row][col]
# moves: "[player][piecetype][currentlocation][destination]" "bbb1a2" -> black bishop from b1 to a2
# players: white = "w", black "b"
# pieces: pawn = "p", rook = "r", bishop = "b", knight = "n", queen = "q", king = you "k"

board = [[]]
board_FEN = ""
board_state = [[], []]


# TODO
def init_board():
    print("Initializing board")
    global board
    board =
    board_FEN = chess.Board()
    print(board)

def reset_board():
    global board
    board = chess.Board()
    print(board)


# TODO later
def convert_file_idx_to_file_letter(file_idx):
    print("temp")


# TODO later
def convert_file_letter_to_file_idx(file_idx):
    print("temp")

# TODO
def convert_square_to_arr_idx(square):
    print("temp")


# TODO later
def convert_arr_idx_to_square(idx):
    print("temp")



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
    print("Calculating board state")


# TODO
def print_board():
    print("temp")
