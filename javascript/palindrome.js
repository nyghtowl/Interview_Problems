/**
Palindrome

Input: word
Output: true if a palindrome

**/

function isPalindrome (word) {
	var half = Math. floor(word.length / 2);
	for (var i=0; i<half; i++) {
		if (word[i]!==word[word.length-1-i]) {
			return false;
		}
	}
	return true;
}

// Test section
isPalindrome('happy');
isPalindrome('aha');