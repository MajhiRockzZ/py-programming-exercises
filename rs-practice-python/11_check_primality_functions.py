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