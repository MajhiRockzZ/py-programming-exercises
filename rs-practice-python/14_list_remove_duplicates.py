"""
---------------------------------------------------------
Exercise 14 :
---------------------------------------------------------
Write a program (function) that takes a list and returns
a new list that contains all the elements of the first
list minus all the duplicates.

---------------------------------------------------------
Extras:
---------------------------------------------------------
    1. Write two different functions to do this - one
    using a loop and constructing a list, and another
    using sets.

---------------------------------------------------------
Concepts :
---------------------------------------------------------
    1. Sets
---------------------------------------------------------
 """


def minus_duplicates(input_list_arr):
    return list(set(input_list_arr))


"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 1 ----->>>>>>>>>
---------------------------------------------------------
 """


def duplicates_remover(arr):
    temp_arr = []
    for ele in arr:
        if ele not in temp_arr:
            temp_arr.append(ele)
    return temp_arr


temp_list_arr = [1, 1, 2, 2, 3, 3, 3]
print(minus_duplicates(temp_list_arr))
print(duplicates_remover(temp_list_arr))
