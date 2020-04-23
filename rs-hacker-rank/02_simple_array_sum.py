# =================
# SIMPLE ARRAY SUM
# =================

""" 
----------------------
PROBLEM
----------------------
Given an array of integers, find the sum of its elements.
For example, if the array ar = [1,2,3], 1 + 2 + 3 = 6, so return 6

----------------------
INPUT FORMATE
----------------------
The first line contains an integer, n denoting the size of the array
The second line contains n space-separated integers representing the
array's elements

----------------------
OUTPUT FORMATE
----------------------
Print the sum of the array's elements as a single integer.

 """

ar = [1, 2, 3]


def simpleArraySum(arr):
    output = 0
    for data in arr:
        output = output + data
    print(output)


simpleArraySum(ar)
