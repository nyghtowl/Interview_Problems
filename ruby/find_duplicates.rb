'''
Find Duplicates

Input: list of Size N, integers from 1 to n
Output: print out if there are duplicates
'''

def find_dup(list1)
	ans = Array.new
	list1.each_with_index do |l, i|
		if i < list1.length
			list2 = list1[i+1,]
			puts list2
			if list2.include? l
				ans << l
			end
		end
	end
	ans
end

if __FILE__ == $0

    # Test section
    input1 = [5,4,7,2,1,8,3,1,4]
    result1 = [1, 4]

    puts "f(%s) == %s: %s" % [input1,result1,(find_dup(input1) == result1)]

end 