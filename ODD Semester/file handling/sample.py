def prime(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            s += 1

    if s == 2:
        print(n, 'is prime')
    else:
        print('Not a prime number ')


# main code
n = 23
out1 = prime(n)
print(out1)
