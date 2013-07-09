'''
Deviation Problem

Input: list of integer elements and an integer (length of sequences)

Consider all the sequences of consecutive elements in the list.For each sequence, compute the difference between the maximum and the minimum value of the elements in that sequence and name it the deviation.

Output: Write a function that computes and returns the maximum value among the deviations of all the sequences  

Constraints: 
* List contains up to 100,000 elements. 
* All the elements are integer numbers in the range: [1, 231 -1]
* Return in less than 2 seconds

Example: The sequences of length 3 are...

    6 9 4 having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
    9 4 7 having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
    7 4 1 having the median 6 (the minimum value in the sequence is 1 and the maximum is 7)
    The maximum value among all medians is 6

Expand: For negative numbers and/or odd sements
'''

def max_deviation(int_list,seq_len):
    marker = 0
    dev_list = []

    while marker < len(int_list):
        segment = int_list[marker:marker+seq_len]
        dev_list.append(max(segment) - min(segment))
        marker += seq_len
    return max(dev_list)

def max_deviation2(int_list,seq_len):
    dev_list = []

    num_seg = int(len(int_list)/(seq_len))

    marker = 0

    for i in range(0, num_seg):
        segment = int_list[marker:marker+seq_len]
        dev_list.append(max(segment) - min(segment))
        marker += seq_len

    return max(dev_list)


# Let's define N as the length of the overall sequence and M is the length of the subsequence.
#
# In a simple approach, where we build a subsequence for each part, we will build O(N - m) subsequences.
# We will then run max() and min() (which are O(M)) N-M times, so the runtime of this implementation is O(NM).
#
# Just knocking this out, pythonically and not worrying about the performance too much:
def max_deviation3(int_list, seq_len):
    last_start_bound = 1 + len(int_list) - seq_len
    subseqs = [int_list[i:i+seq_len] for i in range(0, last_start_bound, seq_len)]
    deviations = [(max(subseq) - min(subseq)) for subseq in subseqs]
    return max(deviations)

#(Remember that list comprehensions are like loops and they are running on a list len(N-M).
# Within that, max/min are also loops running on the shorter O(M) sequences.)

# We can improve slightly by switching to generators so we don't materialize all the
# intermediate structures until needed: (This has the same runtime complexity, but uses less memory.)
def max_deviation4(int_list, seq_len):
    last_start_bound = 1 + len(int_list) - seq_len
    subseqs = (int_list[i:i+seq_len] for i in xrange(0, last_start_bound, seq_len))
    deviations = ((max(subseq) - min(subseq)) for subseq in subseqs)
    return max(deviations)

if __name__ == '__main__':
#Tests
    implementations = [max_deviation, max_deviation2, max_deviation3, max_deviation4]
    int_list = [1, 2, 3, 4, 5, 6]
    seq_len = 2
    result = 1

    int_list2 = [6, 9, 4, 9, 4, 7, 7, 4, 1]
    seq_len2 = 3
    result2 = 6

    int_list3 = [1, 2, 3, 4, 5, 6]
    seq_len3 = 5
    result3 = 4


    for impl in implementations:
        print "trying %s" % impl
        print "  f(int_list, seq_len) == result: %s" % (impl(int_list, seq_len) == result)
        print "  f(int_list2, seq_len2) == result2: %s" % (impl(int_list2, seq_len2) == result2)
        print "  f(int_list3, seq_len3) == result3: %s" % (impl(int_list3, seq_len3) == result3)