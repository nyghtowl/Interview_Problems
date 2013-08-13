'''
Prime Number

Input: positive integer
Output: set of prime divsors of a number

'''

def find_primes(num)
	possible_divisor = 2
	primes = Array.new([])
	while num != 1
		while (num % possible_divisor) == 0
			primes << possible_divisor
			num /= possible_divisor
		end
		possible_divisor += 1
	end
	primes.uniq

end

if __FILE__ == $0

    # Test section
    sample_n = [1,6,7,100]
    results = [[],[2,3],[7],[2,5]]

    sample_n.each_with_index do |n,index|
    	puts "f(%s) == %s: %s" % [n,results[index],(find_primes(n) == results[index])]
    end

end 
