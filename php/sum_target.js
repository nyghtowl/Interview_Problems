/*
Sum Target

Input: List of numbers & target number 
Output: Each pair of numbers that adds up to target

Challenge: 
*For a list of numbers and a target number, return true if any two numbers add to the target number
*Given a list of numbers, return a set of 3 numbers that add to 0.
*/

var sumTarget = function(target, numArray){
	for(i = 0; i < numArray.length; i++) {
		if(numArray.indexOf(target - numArray[i]) != -1){
			return true;
		}
	}
	return false;
}

// Test section
var numArray = [5,3,5,7,1,2,5,6];
var target = 10;

sumTarget(target, numArray);