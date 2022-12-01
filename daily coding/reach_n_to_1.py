"""
This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

"""
# Given a positive integer N, find the smallest number of steps it will take to reach 1
# There are two kinds of permitted steps:
# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

def issquare(n):
    return n**0.5 == int(n**0.5)
N = 10
steps = 0
print(f'{N} >> ', end='')
while N > 1:
    if N % 2 == 0:
        N = N // 2
    else:
        N = N - 1
    steps += 1
    print(f'{N} >> ', end='')
print(f'\n{steps=}')