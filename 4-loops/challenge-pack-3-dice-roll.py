import random

die_1 = random.randint(1,6)
die_2 = random.randint(1,6)
total = die_1 + die_2

answer = int(input('What is the total (2-12)? '))

while answer != total:
    answer = int(input('What is the total (2-12)? '))

print('You got it!')