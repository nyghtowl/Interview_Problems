'''
Fibonacci - each number equals the sum of the two preceding numbers.

Fn = Fn-1 + Fn-2

Input: the point in the sequence to take a fibonnaci number
Output: the fibonnaci number at the point in a sequence starting at 0

Ex: 
At position 0 the Fib number is 0. 
At position 4 the Fib number is 3 (adding 1, 2 which are the numbers before)

Challenge:
* Account for negative or fraction numbers
* Do it more efficiently (memoization)?
* Do it with only O(1) space (iteratively using a for loop)

'''

#O(n)
def impl(position)
	index = 0
	start = 1
	ans = Array.new([0])
	while position > 0
		ans << start
		start += ans[index]
		position -= 1
		index += 1
	end
	ans[-1]
end 

if __FILE__ == $0

    # Test section

    puts "  f(0) == 0: %s" % (impl(0) == 0)
    puts "  f(1) == 1: %s" % (impl(1) == 1)
    puts "  f(2) == 1: %s" % (impl(2) == 1)
    puts "  f(3) == 2: %s" % (impl(3) == 2)
    puts "  f(6) == 8: %s" % (impl(6) == 8)
    puts "  f(13) == 233: %s" % (impl(13) == 233)

end 
