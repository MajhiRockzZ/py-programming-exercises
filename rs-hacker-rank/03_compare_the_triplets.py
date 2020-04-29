# PROBLEM

"""
Alice and Bob each created one problem for HackerRank. 
A reviewer rates the two challenges, awarding points on
a scale from 1 to 100 for three categories: problem clarity,
originality, and difficulty.

We define the rating for Alice's challenge to be the triplet
a = (a[0], a[1], a[2]), and the rating for Bob's challenge to
be the triplet b = (b[0], b[1], b[2]).

Your task is to find their comparison points by comparing
a[0] with b[0], a[1] with b[1], and a[2] with b[2].

=> If a[i] > b[i], then Alice is awarded 1 point.
=> If a[i] < b[i], then Bob is awarded 1 point.
=> If a[i] = b[i], then neither person receives a point

It must return an array of two integers, the first being Alice's
score and the second being Bob's
"""

# EXAMPLE
"""
Sample Input :
5 6 7
3 6 10

Sample Output :
1 1
"""

alice_rating = [5, 6, 7]
bob_rating = [3, 6, 10]

alice_dict = {}
bob_dict = {}

point_table = [0, 0]

for index, element in enumerate(alice_rating):
    alice_dict[f"{index}"] = element

for index, element in enumerate(bob_rating):
    bob_dict[f"{index}"] = element


for index in range(len(alice_dict)):
    if alice_dict[f"{index}"] == bob_dict[f"{index}"]:
        pass
    elif alice_dict[f"{index}"] > bob_dict[f"{index}"]:
        point_table[0] += 1
    elif alice_dict[f"{index}"] < bob_dict[f"{index}"]:
        point_table[1] += 1
    else:
        pass

print(point_table)