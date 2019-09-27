"""
---------------------------------------------------------
Exercise 8:
---------------------------------------------------------
Make a two-player Rock-Paper-Scissors game.
Rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
---------------------------------------------------------
---------------------------------------------------------
Hint : Ask  for player plays (using input), compare them,
  print out a message of congratulation to the winner,
  and ask if the player want to start a new game.
---------------------------------------------------------
---------------------------------------------------------
Concepts :
---------------------------------------------------------
1. While loops
2. Infinite loops
3. Break statements
----------------------------------------------------------
 """

""" user1 = input("What's your name?")
user2 = input("And your name?")

user1_answer = input(f"{user1} do you want to choose rock, paper or scissors?")
user2_answer = input(f"{user2} do you want to choose rock paper or scissors?")


def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper win!")
        else:
            return("Scissors win!")
    else:
        return("Invalid Input! You have not entered rock, paper or scissors, try again.")


print(compare(user1_answer, user2_answer)) """


""" 
---------------------------------------------------------
<<<<<<<------- Alternative Solution ------->>>>>>>>>
---------------------------------------------------------
 """

print("Please pick one: rock⚡ scissors✂ paper📜")

while True:
    game_dict = {
        'rock': 1,
        'scissors': 2,
        'paper': 3
    }

    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over')
            break
    else:
        print('Draw ⚡ Please continue.')
        print('')
