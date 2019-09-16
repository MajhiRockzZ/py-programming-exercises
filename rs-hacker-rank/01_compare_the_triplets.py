def compareTriplets(a, b):
    alice = {}
    bob = {}
    alice_point = 0
    bob_point = 0
    output = []

    for index, element in enumerate(a):
        alice[index] = element

    for index, element in enumerate(b):
        bob[index] = element

    for element in range(0, len(alice)):
        if alice[element] > bob[element]:
            alice_point += 1
        elif alice[element] < bob[element]:
            bob_point += 1
        else:
            alice_point += 0
            bob_point += 0
    output.append(alice_point)
    output.append(bob_point)

    print(output)


compareTriplets([5, 6, 7], [3, 6, 10])
