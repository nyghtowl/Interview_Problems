'''
Find the square root of n.
'''

def sqrt(n)
	(0..n).each do |num|
		if (num * num) == n
			return num
		elsif n < (num * num)
			return "No integer square root."
		end
	end
end



if __FILE__ == $0
	puts sqrt(25) == 5
	puts sqrt(10)
end