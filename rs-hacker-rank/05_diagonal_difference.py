"""
# Diagonal Difference

Given a square matrix, calculate the absolute
difference between the sums of its diagonals.

Example :
1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15.
The right-to-left diagonal = 3 + 5 + 9 = 17.
Their absolute difference is |15 - 17| = 2
 """

matrix_array = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]


def diagonalDifference(arr):
    fd_counter = 0  # forward counter

    bk_counter = len(arr) - 1  # backward counter

    lr_sum = 0  # left to right sum
    rl_sum = 0  # right to left sum

    rs_diff = 0  # resultant difference

    for ar in arr:
        lr_sum += ar[fd_counter]
        rl_sum += ar[bk_counter]

        fd_counter += 1
        bk_counter -= 1

    if lr_sum > rl_sum:
        rs_diff = lr_sum - rl_sum
    elif lr_sum < rl_sum:
        rs_diff = rl_sum - lr_sum

    return rs_diff


print(diagonalDifference(matrix_array))
