'''
Reverse 

Input: string, sentenece or link

Out: reverse of what is submitted

'''

# O(n)
def reverse_str(word)
    return word.reverse!
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
end 

