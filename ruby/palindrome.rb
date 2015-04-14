'''
Palindrome

Input: word
Output: true if a palindrome

'''

# Standard Ruby class and check for reverse string
class Word

    def palindrome?(string)
        string == string.reverse
    end

end

# Alternative Ruby class to inherit from string class and check for reverse string

class Word2 < String

    def palindrome?
        self == self.reverse
    end

end


if __FILE__ == $0
	# Test section
	w = Word.new # Create new instance

	inputs = ["anagram", "laal"]
	results = [false, true]


	inputs.each_with_index {|input, index|
		ans = w.palindrome?(input) == results[index]
		puts "%s(#{input.reverse}) == %s : %s" % ['palindrome?', results[index], ans]
	}
end
