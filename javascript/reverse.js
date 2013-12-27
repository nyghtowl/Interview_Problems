/**
Reverse 

Input: string, sentence or link

Out: reverse of what is submitted

**/

var reverse = function(orig){
	var result = [];
	for (var i = orig.length; i >= 0 ;i--){
		result.push(orig[i]);
	}
	console.log(result.join(""));
}


// Test section
reverse("Hello");