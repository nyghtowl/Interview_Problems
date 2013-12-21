""" 
Product integers

This function takes in a list of integers and returns a list of integers containing the product of the 
# rest of the integers, excluding the corresponding element from the original list of integers. 

Examples:
Input = [1,2,3,4]
Output = [24,12,8,6]

Input = [-1,3,4,2]
Output = [24,-8,-6,-12]

SOLUTION:
Runtime: O(n)
Step1: I multiply every element in the input list1 and store in variable "product."
Step 2: Then, I divide out each element in input list1, append quotient to new_list, and finally, 
return new_list. """

def multiplication(list1):
    product = 1
    for j in list1:
        product = product * j
    return product

def product_intgers(list1):
    # Remove any and all zeros from list1. Any # divided by zero is undefined.
    zero_indices = []
    for i in range(len(list1)):
        if list1[i] == 0:
            zero_indices.append(i)
    for i in zero_indices:
        list1.remove(0)

    product = multiplication(list1)
    new_list = []

    if len(list1) <= 1: # if list1 only contains 1 element or fewer, return the original list1 
        print list1
        return list1

    for i in list1:
        new_list.append(product/i)
    print new_list
    return new_list

if __name__ == '__main__':
    # Sample Test Cases below.
    product_intgers([9]) #Expect [9]
    product_intgers([2,1,0]) # Expect [1,2]
    product_intgers([2,1,0]) #Expect [1,2]
    product_intgers([1,2,3]) #Expect [6,3,2]
    product_intgers([1,2,3,4]) #Expect [24,12,8,6]
    product_intgers([1,2,3,4,5]) #Expect [120,60,40,30,24]
    product_intgers([1,2,3,4,-5]) #Expect [-120,-60,-40,-30,24]
    product_intgers([0,0,0,0,0,0,0,0,0,0,0,0,0]) #Expect [0]