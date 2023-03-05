import learn as learn
import chess
import numpy
import pandas

# board: board[rank][file] [row][col]
# moves: "[player][piecetype][currentlocation][destination]" "bbb1a2" -> black bishop from b1 to a2
# players: white = "w", black "b"
# pieces: pawn = "p", rook = "r", bishop = "b", knight = "n", queen = "q", king = you "k"

board = [[]]
turn = 0
is_whitetomove = True
is_blacktomove = True


# done
def init_board():
    print("Initializing board\n")

    global board
    global turn

    board = [["  "]*8 for i in range(8)]
    turn = 0

    for x in range(8):
        board[1][x] = "wp"
        board[6][x] = "bp"

    board[0][0] = "wr"
    board[7][0] = "br"

    board[0][1] = "wn"
    board[7][1] = "bn"

    board[0][2] = "wb"
    board[7][2] = "bb"

    board[0][3] = "wq"
    board[7][3] = "bq"

    board[0][4] = "wk"
    board[7][4] = "bk"

    board[0][5] = "wb"
    board[7][5] = "bb"

    board[0][6] = "wn"
    board[7][6] = "bn"

    board[0][7] = "wr"
    board[7][7] = "br"

    print_board()


# done
def convert_file_idx_to_file_letter(file_idx):
    file = "x"

    if file_idx == 0:
        file = "a"
    elif file_idx == 1:
        file = "b"
    elif file_idx == 2:
        file = "c"
    elif file_idx == 3:
        file = "d"
    elif file_idx == 4:
        file = "e"
    elif file_idx == 5:
        file = "f"
    elif file_idx == 6:
        file = "g"
    elif file_idx == 7:
        file = "h"

    return file


# done
def convert_file_letter_to_file_idx(file_idx):
    file = -1

    if file_idx == "a":
        file = 0
    elif file_idx == "b":
        file = 1
    elif file_idx == "c":
        file = 2
    elif file_idx == "d":
        file = 3
    elif file_idx == "e":
        file = 4
    elif file_idx == "f":
        file = 5
    elif file_idx == "g":
        file = 6
    elif file_idx == "h":
        file = 7

    return file


# done
def convert_square_to_arr_idx(square):
    idx = []
    file_idx = convert_file_letter_to_file_idx(square[0])
    rank_idx = int(square[1])
    idx.append(rank_idx)
    idx.append(file_idx)


# done
def convert_arr_idx_to_square(idx):

    square = ""
    file = convert_file_idx_to_file_letter(idx[1])
    rank = idx[0]
    square = square + file + rank

    return square


# done
def find_existing_pieces(piece_type, player):

    global board
    piece_locations = []
    for idx_rank, rank in enumerate(board):
        for idx_file, square in enumerate(rank):
            if square == player + piece_type:
                piece_locations.append([idx_rank, idx_file])

    return piece_locations


# TODO
def is_legal_move(move):

    global board
    global turn
    global is_whitetomove
    global is_blacktomove

    # [islegalmove, player, piece type, current location, destination square]
    is_lm = [False, "", "", [], []]

    player = move[0]
    piece_type = move[1]


    # blocks, current checks, future checks, illegal movement types, does current piece exist

    return is_lm


# done
def get_turn_move(move):

    global board
    global turn
    global is_whitetomove
    global is_blacktomove

    legal_move = is_legal_move(move)
    is_lm = legal_move[0]

    if is_lm:
        player = legal_move[1]
        piece = legal_move[2]
        current_location = legal_move[3]
        destination = legal_move[4]

        board[destination[0]][destination[1]] = player + piece
        board[current_location[0]][current_location[1]] = "  "

        if is_blacktomove:
            turn += turn

        is_whitetomove = not is_whitetomove
        is_blacktomove = not is_blacktomove
    else:
        print("This is not a legal move")


# TODO
def calc_board_state():
    print("Calculating board state")


# done
def print_board():

    global board

    white_square = "  "
    black_square = "[]"
    square_color = [white_square, "w"]
    opposite_square_color = black_square

    # "   A  B  C  D  E  F  G  H \n"
    # "8 [ ]   [ ]   [ ]   [ ]   \n"
    # "7    [ ]   [ ]   [ ]   [ ]\n"
    header_string = "     A   B   C   D   E   F   G   H    \n  ------------------------------------"
    footer_string = "  ------------------------------------"

    print(header_string)

    # print("   ", end = "")
    # for x in range(8):
    #   print(f"{convert_file_idx_to_file_letter(x)}  ", end = "")
    # print()

    num_ranks = len(board)
    for idx_rank, rank in enumerate(reversed(board)):
        print(f"{num_ranks} | ", end = "")
        num_ranks -= 1


        for idx_file, square in enumerate(rank):
            print(f"{square_color[0][0]}{square}{square_color[0][1]}", end = "")

            # swap square color
            if idx_file < 7:
                temp = square_color[0]
                square_color[0] = opposite_square_color
                opposite_square_color = temp

        print(" |")

    print(footer_string)