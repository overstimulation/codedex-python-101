import random

question = input("Enter any Yes/No question: ")

random_number = random.randint(0, 8)

if random_number == 8:
  print('Yes - definitely.')
elif random_number == 7:
  print('It is decidedly so.')
elif random_number == 6:
  print('Without a doubt.')
elif random_number == 5:
  print('Reply hazy, try again.')
elif random_number == 4:
  print('Ask again later.')
elif random_number == 3:
  print('Better not tell you now.')
elif random_number == 2:
  print('My sources say no.')
elif random_number == 1:
  print('Outlook not so good.')
elif random_number == 0:
  print('Very doubtful.')