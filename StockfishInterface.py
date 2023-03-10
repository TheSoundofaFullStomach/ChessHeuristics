import stockfish as Stockfish
import Board


class StockfishInterface:

    # GLOBAL
    test = ""
    stockfish = ""

    def __init__(self):
        print("stockfish interface")

        # self.stockfish = Stockfish()

    def get_move(self, board):
        print("stub")
