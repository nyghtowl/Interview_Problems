'''
Find Duplicates

Input: list of Size N, integers from 1 to n
Output: print out if there are duplicates
'''

# O(n^2)
def find_dup(list1)
	ans = Array.new
	list1.each_with_index do |l, i|
		len = list1.length
		if i < len
			if list1[i+1..len].include?(l)
				ans << l
			end
		end
	end
	ans.sort
end

if __FILE__ == $0

    # Test section
    input1 = [5,4,7,2,1,8,3,1,4]
    result1 = [1, 4]

    puts "f(%s) == %s: %s" % [input1,result1,(find_dup(input1) == result1)]

end 