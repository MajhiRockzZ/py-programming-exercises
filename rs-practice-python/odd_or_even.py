""" 
---------------------------------------------------------
Exercise 1 : 
---------------------------------------------------------
Ask the user for a number. Depending on wheteher the 
number is even or odd, print out an appopriate message 
to the user.
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. Modular Operator --> %
2. Conditionals --> if/else/while/elif
3. Equality --> ==/!==/===/!=
----------------------------------------------------------
 """

num = int(input(f"Enter any number of your choice? : "))

if num % 2 == 0:
    print(f"{num} is a even number.")
else:
    print(f"{num} is a odd number.")
