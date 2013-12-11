'''
Sum Target / Combination Validation

n is an int

Returns True if some integer combination of 6, 9 and 20 equals n
Otherwise returns False.

'''

def target_combo(n)
	combo_sizes = [20, 9, 6]
	remaining = n

	combo_sizes.each do |size|
		remaining -= (remaining / size) * size
	end

	return remaining == 0
end



if __FILE__ == $0

	# Test section
	puts "f(6) is %s" % [target_combo(6)==true]
	puts "f(7) is %s" % [target_combo(7)==false]


end

