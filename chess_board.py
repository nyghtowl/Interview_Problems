''' 
chess board

draw a chess board - w & b assume drawwhite and drawblack functions exist and
can be called

chessboard is 8 x 8 but to make this function more usable, better to use a
variable for size

trick - when drawn out, when the numbers on a grid are both even or both odd then they are the same color

'''

def draw_board(n):
    for i in range(8):
        for j in range(8):
            if (i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0):
                draw_white()
            else:
                draw_black()
#---

def is_even(c):
    return c % 2 == 0

def draw_board2(n):
    for row in range(n):
        for column in range(n):
            if is_even(row):
                if is_even(column):
                    draw_white()
                else:
                    draw_black()
            else:
                if is_even(column):
                    draw_black()
                else:
                    draw_white()                

#---

#micro-optimizing to show off nested list comprehensions. - jdunck
#  in the 1st row, make the odd checks black.
#  in the 2nd row, make the even checks black.
def draw_board3(n):
    boxes = [(i,j) for i in range(n) for j in range(n)]
    for box in boxes:
        if is_even(box[0] + box[1]):
            draw_white()
        else:
            draw_black()
