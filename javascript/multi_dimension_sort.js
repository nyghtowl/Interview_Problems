/**
*Sort two dimensional array 
*/

var array = [[9,8], [2,3], [4,5], [3,4]]

array.sort(function(a,b){if (a[0]<b[0]){return -1;} else {return 1;} return 0; });