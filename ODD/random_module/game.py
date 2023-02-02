
import random
num = random.randint(1, 100)
attempts = 10
while attempts:
    user_num = int(input('Guess the Number Between 1 to 100 '))
    attempts -= 1
    print(f'Number of attemps left{attempts}')
    if user_num < num:
        print('Too Small')
    elif user_num > num:
        print('Too Large')
    else:
        print('You Won!')
        break
else:
    print(f'You failed to Guess the number {num}')