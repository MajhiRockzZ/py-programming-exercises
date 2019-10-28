"""
---------------------------------------------------------
Exercise 15 :
---------------------------------------------------------
Write a program (using functions!) that asks the user for
a long string containing multiple words. Print back to the
user the same string, except with the words in backwrds
order. eg: <<< My name is Michele
            >>> Michele is name My
---------------------------------------------------------
Concepts :
---------------------------------------------------------
    1. More string things.
---------------------------------------------------------
 """

input_string = input(f"Please enter a string input ?")

def string_reversal(input_string):
    string_arr = input_string.split()
    reversed_string = ""
    for word in input_string:
        reversed_string = word + reversed_string
    return reversed_string

result = string_reversal(input_string)
print(result)
