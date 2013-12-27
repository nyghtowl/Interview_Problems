/**
* Multi-dimension Sort 

Input: two dimensional array 
Output: 
*/

var table = [[9,8], [2,3], [4,5], [3,4]]

function dimension_sort(table){
	return table.sort( function(a,b){
		if (a[0]<b[0]){
			return -1;
		} else {
			return 1;
		} 
		return 0; 
	});	
}

//Test section
dimension_sort(table);