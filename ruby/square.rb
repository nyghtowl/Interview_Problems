''' 
Square

Input: number
Ouput: number squared
'''

# Simple - O(1)
def square(num)
	num * num
end

# Loop - O(n)
def square2(num)
	result = []
	if num != 0
		(0...num).each do |n|
			result << num
		end
		result.inject(:+)
	else
		num
	end
end

if __FILE__ == $0

	# Test section
	puts 'square'
	puts "f(0) == 0: %s" % [square(0) == 0]
	puts "f(1) == 1: %s" % [square(1) == 1]
	puts "f(2) == 4: %s" % [square(2) == 4]
	puts "f(3) == 9: %s" % [square(3) == 9]
	puts "f(10) == 100: %s" % [square(10) == 100]


	puts 'square2'
	puts "f(0) == 0: %s" % [square2(0) == 0]
	puts "f(1) == 1: %s" % [square2(1) == 1]
	puts "f(2) == 4: %s" % [square2(2) == 4]
	puts "f(3) == 9: %s" % [square2(3) == 9]
	puts "f(10) == 100: %s" % [square2(10) == 100]
end 

