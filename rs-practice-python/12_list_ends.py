"""
---------------------------------------------------------
Exercise 12:
---------------------------------------------------------
Write a program that takes a list of numbers (for example,
 a = [5, 10, 15, 20, 25]) and makes a new list of only the
  first and last elements of the given list.
---------------------------------------------------------
Concepts :
---------------------------------------------------------
1. Lists and properties of lists
2. List comprehensions
3. Functions
----------------------------------------------------------
 """

def array_generator(int_input, rate):
    output_array = []
    arr_ele = 0
    while rate > 0:
        arr_ele = arr_ele + int_input
        output_array.append(arr_ele)
        rate = rate - 1
    return output_array

random_arr = array_generator(4, 8)

def machine(input_arr):
    output_arr = []

    first_ele = input_arr[0]
    last_ele = input_arr[len(input_arr) - 1]

    output_arr.append(first_ele)
    output_arr.append(last_ele)

    return output_arr

print(random_arr)
print(machine(random_arr))