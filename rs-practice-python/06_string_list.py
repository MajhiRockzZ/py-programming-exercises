""" 
---------------------------------------------------------
Exercise 5 : 
---------------------------------------------------------
Ask the user for a string and print out whether this 
string is a palindrome or not. (A palindrome is a string
that reads the same forwards and backwards.)
---------------------------------------------------------
Concepts : 
---------------------------------------------------------
1. List Indexing --> We starts counting lists from the
  number 0.
2. Strings are lists --> We can do to string everything
  that we can do to list.
----------------------------------------------------------
 """

name = str(input(f"What is your good name? : "))
# name = "Sumesh"
# print(f"Hello {name}, nice to meet you!")
reverse = ''
for character in name:
    reverse = character + reverse

if reverse == name:
    print(f"The string {name} is an palindrome.")
else:
    print(f"The string {name} is not an palindrom, Please try another string.")

# print(reverse)
""" 
---------------------------------------------------------
Solution: Using the string reversal
---------------------------------------------------------
 """

wrd = input("Please enter a word")
wrd = "Sumesh"
wrd = str(wrd)
rvs = wrd[::-1]
# print(rvs)
if wrd == rvs:
    print(f"{wrd} is a palindrom")
else:
    print(f"{wrd} is not a palindrom")

""" 
---------------------------------------------------------
Solution: Using for loops
---------------------------------------------------------
 """
