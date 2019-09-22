""" 
---------------------------------------------------------
Exercise 5 : 
---------------------------------------------------------
Let's say I gave you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one 
line of Python that takes this list a and makes a new 
list that has only the even elements of this list in it
-----------------------------------------7---------------
Concepts : 
---------------------------------------------------------
1. List comprehensions: The idea of list comprehension 
  is to make code more compact to accomplish tasks involving 
  lists. 
  eg: ages = [2014 - year for year in year_of_birth]
----------------------------------------------------------
 """
import random
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [element for element in a if element % 2 == 0]
print(b)

""" 
---------------------------------------------------------
<<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

numlist = []
list_length = random.randint(5, 15)

print(list_length)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))


# print(numlist)

evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)
