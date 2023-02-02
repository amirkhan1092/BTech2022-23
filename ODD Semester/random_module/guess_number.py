# 
import random
num = random.randint(1, 100)
attempts = 10
while attempts:
    user_num = int(input('Guess the number 1 to 100 '))
    print(f'Attempts left {attempts}')
    attempts -= 1
    if user_num == num:
        print('You Won!', 'with score', attempts)
        break
    elif user_num < num:
        print('Too Small')
    else:
        print('Too Large')
else:
    print('You failed to guess the number ')        