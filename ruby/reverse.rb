'''
Reverse 

Input: string, sentence or link

Out: reverse of what is submitted

'''

# O(n)
def reverse_str(word)
    word.reverse
end

def reverse_str2(word)
	len = word.length
	half_len = (len/2) - 1
	(0..half_len).each do |i|
		len -= 1
		temp = word[i]
		word[i] = word[len]
		word[len] = temp
	end
	word
end

if __FILE__ == $0

	# Test section
	implementations = ['reverse_str', 'reverse_str2']
	inputs = ['stressed', 'hello']
	results = ['desserts', 'olleh']
	
	inputs.each_with_index {|input, index|
		ans = reverse_str(input) == results[index]
		puts "%s(#{input.reverse}) == %s : %s" % ['reverse_str', results[index], ans]
	}

	inputs.each_with_index {|input, index|
		ans = reverse_str2(input) == results[index]
		puts "%s(#{input.reverse}) == %s : %s" % ['reverse_str2', results[index], ans]
	}
end 

