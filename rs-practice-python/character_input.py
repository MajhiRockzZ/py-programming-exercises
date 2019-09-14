""" 
---------------------------------------------------------
Exercise 1 : 
---------------------------------------------------------
Create a program that asks the user to enter their name 
and their age. Print out a message addressed to them that 
tells them the year that they will turn 100 years old.
---------------------------------------------------------
1. input() --> To get user input in Python 3.
2. int() --> Turn the string into an integer.
3. str() --> Turn integer into strings.
----------------------------------------------------------
 """

import datetime

name = input(f"Give me your name? : ")
age = int(input(f"Now, Give me your age? : "))

current_year = datetime.datetime.now().year

year = ((current_year - age) + 100)

print(f"{name} will be 100 years old in the year {year}")
