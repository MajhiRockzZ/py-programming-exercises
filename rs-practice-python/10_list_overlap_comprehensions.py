"""
---------------------------------------------------------
Exercise 10:
---------------------------------------------------------
Take two list, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

  and write a program that returns a list that contains
  only the elements that are common between the lists
  (without duplicates). Make sure your program works on
  two list of different sizes. Write this using at least
  one list comprehension. 
---------------------------------------------------------
---------------------------------------------------------
Hint : 
---------------------------------------------------------
  1. Use list comprehensions
---------------------------------------------------------
---------------------------------------------------------
Extra :
---------------------------------------------------------
  1. Randomly generate two lists to test this
----------------------------------------------------------
 """

import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(100), 11)
b = random.sample(range(200), 15)

print(a)
print(b)

r = []

for element_a in a:
    if element_a in b:
        r.append(element_a)

print(set(r))

""" 
---------------------------------------------------------
  <<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result = [i for i in a if i in b]

print(result)

""" 
---------------------------------------------------------
  <<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 39), 16)
result = [i for i in set(a) if i in b]

""" 
---------------------------------------------------------
  <<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
    if element not in result:
        result.append(element)

print(result)

""" 
---------------------------------------------------------
  <<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result_overlap = [i for i in set(a) if i in b]
result = [i for i in result_overlap if result_overlap.count(i) == 1]
