'''
Tic Tac Toe
3 X 3 

all xs or os

game over 3 in a row

Board Class

class Board(object):
    X = 'x'
    O = 'o'
    def __init__(self):
        self.board = [[None] * 3] * 3
    def play(self, row, col, side):
        if self.board[row][col] is not None:
            raise ValueError
        self.board[row][col] = side
        self.checkWin()
    def checkWin(self):
        # walk 3 in a direction

b = Board()
b.play(1, 1, Board.X)

'''