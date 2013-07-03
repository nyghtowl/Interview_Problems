list = [5,3,7,5,1,2,5,6]
target = 10

def add(list, target):
	#make a dictionary of nums in the list
	#to make the lookup faster
	num_dict = {}
	for i, num in enumerate(list):
		if num not in num_dict:
			num_dict[num] = [i]
		else:
			num_dict[num].append(i)

	# now go through each number in the list
	for i, num in enumerate(list):
		diff = target - num

		#this is for, for example, 
		#if you're looking for 10
		#and you get a 5 in the list
		#you need another 5
		if diff == num:
			if len(num_dict[num]) > 1:
				return True
		#look for the difference in the dict. 
		#if it's there then you've got
		#your sum
		if diff in num_dict:
			return True
	return False

# putting the list in a dictionary first
# passes through the list once, giving it 
# a time of n, then going through the 
# the list again is another n which makes
# 2n. Since integers don't matter much 
# it's n time. 







l1 = [5,4,7,2,1,8,3]
l2 = [8,1,2,7,5,3]
# missing number = 4

def missing(l1, l2):
	l1.sort()
	l2.sort()

	if len(l1) > len(l2):
		longest = l1
		second = l2
	else:
		longest = l2
		second = l1


	for i, num in enumerate(longest):
		if i == len(longest)-1:
			return longest[i]
		elif num != second[i]:
			return num

# This is bad n time because the sort algorithm takes 
# some amount of time (i don't know because it's set
# by the programming language, then n again to go through
# the list again.)

# The best way to do it is add both lists up
# and subtract them 
# sum(l1) = 30
# sum(l2) = 26
# difference is 4 :)

