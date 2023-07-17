
# two sum
lst = [1, 2, 3, 6]
target = 5

d = {}
for i, num in enumerate(lst):
    if target - num in d:
        print([d[target - num], i])
        break
    d[num] = i
