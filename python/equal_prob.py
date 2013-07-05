'''
Equal Probability
Shuffle a string to make sure that it returns an equal-probability. Basically, for string of length n, you have n! permutations-- so the string you return should reflect 1/n!. What I did was pick a random number between (i, n-1) and increment i until it reaches len(string)-1, then take that random index and swap it with the first character of the string. As you iterate, you only look at the slice of string (i: len(string)-1) because the swapped characters (ones in the front) have been used already, and shouldn't be touched again.
'''