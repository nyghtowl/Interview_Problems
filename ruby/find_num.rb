'''
Find Num 

Input: List of integers and target number.
Output: What number is missing. Must determine if the missing number is positive or negative

'''
# O(n^2)
def find_miss_num(list1, list2)
	larger_list = [list1, list2].max
	smaller_list = [list1, list2].min

	result = Array.new 

	smaller_list.each do |num|
		unless larger_list.include?(num)
			result << num
		end
	end
	return result

end


if __FILE__ == $0
	# Test section
	list1 = [5,4,7,2,8,3]
	list2 = [5,4,7,2,1,8,3]
	list3 = [9,-1,10,2,300,3,0,-10]

	print "f(list1, list2) == 1 is %s" % [find_miss_num(list1, list2) == [1]]
	puts
	print "f(list1, list3) == 5, 4, 7, 8 is %s" % [find_miss_num(list1, list3) == [5, 4, 7, 8]]
	puts

end