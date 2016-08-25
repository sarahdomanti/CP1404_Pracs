import random

MAXIMUM = 45

quick_pick_num = int(input("How many quick picks? "))
for i in range(quick_pick_num):
    numbers = []
    for j in range(6):
        num = random.randint(1, MAXIMUM)
        while num in numbers:
            num = random.randint(1, MAXIMUM)
        numbers.append(num)
    numbers.sort()
    for num in range(len(numbers)):
        print('{:>3}'.format(numbers[num]), end=' ')
    print('\n', end='')
