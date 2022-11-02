

for num in range(1, 101):
    s = 0
    for i in range(1, num+1):
        if num % i == 0:
            s += 1
    if s == 2:
        print(num, end=' ')