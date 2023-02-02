
num = int(input('Enter the positive Integer '))
s = 0
for i in range(1, num+1):
    if num % i == 0:
        s += 1

if s == 2:
    print(num, 'is prime')
else:
    print('Not a prime number ')      