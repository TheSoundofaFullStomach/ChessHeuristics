from StockfishInterface import StockfishInterface
from HumanInterface import HumanInterface
import Board

class OpponentInterface:

    # GLOBAL
    opponent_interface = ""

    def __init__(self, opponent_code):

        if opponent_code == 1:
            self.opponent_interface = StockfishInterface()
            print("I will play stockfish")
        elif opponent_code == 2:
            self.opponent_interface = HumanInterface()
            print("I will play you")
        else:
            self.opponent_interface = StockfishInterface()
            print("I will play stockfish")

    def get_move(self, board):
        return self.opponent_interface.get_move(board)


