gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input('Q1) Do you like Dawn or Dusk?\n\t1) Dawn\n\t2) Dusk\n'))
if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Wrong input.')

q2 = int(input('Q2) When I’m dead, I want people to remember me as:\n\t1) The Good\n\t2) The Great\n\t3) The Wise\n\t4) The Bold\n'))
if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print('Wrong input.')

q3 = int(input('Q3) Which kind of instrument most pleases your ear?\n\t1) The violin\n\t2) The trumpet\n\t3) The piano\n\t4) The drum\n'))
if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print('Wrong input.')

print(f'Final scores:\nGryffindor: {gryffindor}\nRavenclaw: {ravenclaw}\nHufflepuff: {hufflepuff}\nSlytherin: {slytherin}')

scores = [0,0,0,0]
scores[0] = gryffindor
scores[1] = ravenclaw
scores[2] = hufflepuff
scores[3] = slytherin
scores.sort()
print(f'House with the most points: {scores[3]}')