""" 
+++++++++++++++
A Very Big Sum
+++++++++++++++

# Problem

Calculate and print the sum of the elements in an array.
keeping in mind that some of those integers may be quite
large.

# Sample Input
5
1000000001 1000000002 1000000003 1000000004 100000005

# Output
500000015
 """

def aVeryBigSum(ar):
    result = 0
    for ele in ar:
        result += ele
    return result


print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 100000005]))
