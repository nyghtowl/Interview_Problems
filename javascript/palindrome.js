// Check if a given word is a palindrome (same forward and backwards)

function isPalindrome (word) {
	var half = Math. floor(word.length / 2);
	for (var i=0; i<half; i++) {
		if (word[i]!==word[word.length-1-i]) {
			return false;
		}
	}
	return true;
}