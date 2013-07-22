Tic-tac-toe

class Board():
    def __init__(self):
        self._b=[
        [Tile(None), Tile(None), Tile(None)]
        [Tile(None), Tile(None), Tile(None)]
        [Tile(None), Tile(None), Tile(None)]
        ]
    def play(self, piece, row, col):
        r = self._b[row]
        r[col] = piece

        OR 

        self._b[row][col] = piece

    def score(self, row, col):
        return self._b[row][col]

class Tile():
    def __init__(self, val):
        self.val = val


b = Board()
player = "X"
while b.score()==None:
    row = raw_input("row?")
    col = raw_input("column?")
    b.play(player, row, col)
    if player =="X":
        player = "O"
    else:
        player = "X"

print "Player", b.score(), "wins!"
