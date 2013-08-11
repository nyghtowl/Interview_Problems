'''
List Intersection

Input: 2 lists
Output: numbers where the two lists intersect 
'''

# O(n^2) 
def list_int(list1, list2)
	response = Array.new ([])
	list1.each do |num|
		if list2.include? num
			response << num
		end
	end
	response 
end

if __FILE__ == $0

    # Test section
    list1 = [9,-1,10,2,300,3,0,-10]
    list2 = [5,4,7,-1,8,9]
    list3 = [-2,2000,30,16,85,903,567,4] 
    results1 = [9,-1]
    results2 = []

    ans1 = list_int(list1, list2) == results1
    ans2 = list_int(list1, list3) == results2
    puts "%s == %s : %s" % ['list intersection', results1, ans1]
    puts "%s == %s : %s" % ['list intersection', results2, ans2]
end 
