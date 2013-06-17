'''
rotate the matrix


1 2 3
4 5 6 
7 8 9

switch to 

7 4 1
8 5 2
9 6 3

'''

function rotateMatrix(matrix) {
    for(row=0; row<=matrix.length(); row++){
        for(col=0; col<=matrix.length; col++){
            new matrix = [[],[],[]];
            temp val = matrix[row][col]
            new matrix[col]
        }
    }
}

# assume data structure is a list of coordinates for the numbers

def flip_matrix(mat):
    # needed a midpoint lenght to compare to but could just set 1 or 2 depending on if coord start at 0,0 or 1,1
    mid = int(len(matrix/6))
    for i, coord in enumerate(matrix):
        if i == 0:
            pass
        # if x is 1 then it just flips x & y
        elif mid == coord[0]:
            coord[0], coord[1] = coord[1], coord[0]
        # if x is less than 1 then x becomes y and y becomes 2
        elif mid > coord[1]:
            coord[0] = coord[1]
            coord[1] = mid + 1
        # if x is greater than 1 then x becomes y and y becomes 1
        elif mid < coord[0]:
            coord[0] = coord[1]
            coord[1] = mid - 1

var: x1, x2, y1, y2
newMatrix = []
for(var i=1; i <= matrix.length(); i++){
    newMatrix.push[()];
}
for(y1=0, y2=matrix.length-1; y1<= matrix.length;, y2>=; y1++, y2--){
    for(x1=0, x2=matrix[y1].length; x<=matrix[y1].length), x2>=0; x1++, x2--){
    newMatrix[x1][y2] = matrix[y1][x1];
    }
    return newMatrix;
}

# better way new[x,y] = old [y,2-x]