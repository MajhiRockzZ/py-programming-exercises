""" 
---------------------------------------------------------
Exercise 6 : 
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
rvs = wrd[::-1]  # To reverse a string
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


def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x


word = "tnt"
# word = input(f"give me a word:\n")
x = reverse(word)
if x == word:
    print(f"This is a Palindrome")
else:
    print(f"This is NOT a Palindrom")
    """ Always getting not an palindrom need explanation """
