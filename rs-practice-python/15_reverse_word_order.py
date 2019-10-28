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

# input_string = input(f"Please enter a string input : ")


def string_reversal(input_str):
    string_arr = input_str.split()
    reversed_string = " "
    for word in string_arr:
        reversed_string = f"{word} {reversed_string}"
    return reversed_string


# result = string_reversal(input_string)
# print(result)

"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 1 ----->>>>>>>>>
---------------------------------------------------------
 """


def reverseWord(w):
    return ' '.join(w.split()[::-1])


"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 2 ----->>>>>>>>>
---------------------------------------------------------
 """


def reverse_v1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0, word)
    return " ".join(result)


"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 3 ----->>>>>>>>>
---------------------------------------------------------
 """


def reverse_v2(x):
    y = x.split()
    return " ".join(y[::-1])


"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 4 ----->>>>>>>>>
---------------------------------------------------------
 """


def reverse_v3(x):
    y = x.split()
    return " ".join(reversed(y))


"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 5 ----->>>>>>>>>
---------------------------------------------------------
 """


def reverse_v4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


test1 = input("Enter a sentence : ")
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))
print(reverseWord(test1))
