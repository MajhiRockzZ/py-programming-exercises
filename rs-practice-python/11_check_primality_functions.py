"""
---------------------------------------------------------
Exercise 11:
---------------------------------------------------------
Ask the user for a number and determine whether the number
is prime or not. Take this opportunity to practice using
functions
---------------------------------------------------------
Concepts :
---------------------------------------------------------
1. Functions
2. Reusable functions
3. Default arguments

eg: def get_integer(help_text="Give me a number: "):
    # -- Example for default arguments and function 👆--
        return int(input(help_text))

    # -- Example for reusable functions 👇--
    age = get_integer("Tell me your age: ")
    school_year = get_integer()

    if age > 15:
        print(f"You are over the age of 15")

    print(f"You are in grade {school_year}")
----------------------------------------------------------
 """

def check_prime(input_value = "Enter a number to check : "):
    int_input = int(input(input_value))

    temp_input = int_input

    counter = 0

    while temp_input > 0:
        if(int_input % temp_input == 0):
            counter = counter + 1
        temp_input = temp_input - 1

    if counter == 2:
        print(f"It's a prime number!")
    else:
        print(f"It's not a prime number!")

check_prime()

"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 1 ----->>>>>>>>>
---------------------------------------------------------
 """
def get_number(prompt):
    return int(input(prompt))

def is_prime(number):
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for check_number in range(2, (number / 2)-1):
            if number % check_number == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number, " is", descriptor, "prime.", sep = "", end = "\n\n")

while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctl-C to exit."))

"""
---------------------------------------------------------
  <<<<<<<----- Alternative Solution : 2 ----->>>>>>>>>
---------------------------------------------------------
 """
import sys
number = input("Please enter a number" + "\n" + ">>>")
number = int(number)
prime = False
if number > 0:
    for x in range(2, number - 1):
        if number % x != 0:
            continue
        elif number % x == 0:
            sys.exit("The number is not prime.")
    sys.exit("The number is prime.")
elif number == 0:
    sys.exit("The number is not prime.")
else:
    sys.exit("The number is not prime.")