/**
Turn Matrix

Given an 3x3 matrix, rotate the matrix by 90 degrees and return rotated matrix.
Example:

1 2 3
4 5 6 
7 8 9

switch to 

7 4 1
8 5 2
9 6 3

**/
#Javascript example solution 
function rotateMatrix(matrix) {
    for(row=0; row<=matrix.length(); row++){
        for(col=0; col<=matrix.length; col++){
            new matrix = [[],[],[]];
            temp val = matrix[row][col]
            new matrix[col]
        }
    }
}

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
