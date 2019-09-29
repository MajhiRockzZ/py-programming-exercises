"""
---------------------------------------------------------
Exercise 9:
---------------------------------------------------------
Generate a random number between 1 and 9 (including 1 and
   9). Ask the user to guess the number, then tell them 
   whether they guessed too low, too hight, or exactly right.
---------------------------------------------------------
---------------------------------------------------------
Hint : 1. Use the user input
       2. import random 
       3. use random.randint(a, b) 

---------------------------------------------------------
---------------------------------------------------------
Concepts :
---------------------------------------------------------
1. Modules
2. Random numbers
3. User input
----------------------------------------------------------
 """

import random

random_num = random.randint(1, 9)

print(random_num)


while True:
    guessed_num = int(
        input(f"Guess a number between 1 and 9, I will tell you how close you are!"))
    if guessed_num == random_num:
        print(f"Awesome! you gussed exactly the right number🤑")
        break
    elif guessed_num > random_num:
        print(f"Your guess is too high, no problem you can try again😎")
        continue
    elif guessed_num < random_num:
        print(f"Your guess is to low, please try again😣")
        continue

""" 
-------------------------------------------------------------
Extras :
-------------------------------------------------------------
1. Keep the game going until the user types "exit"

2. Keep track of how many guesses the user has taken, and 
   when the game ends, print this out.
-------------------------------------------------------------
 """


number = random.randint(1, 9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("What's your guess?")

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high")
    else:
        print("You got it!")
        print(f"And it only took you {count} tries!")
