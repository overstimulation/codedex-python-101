class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

mcdonalds = Restaurant()
mcdonalds.name = 'McDonald\'s'
mcdonalds.category = 'Fast Food'
mcdonalds.rating = 4.5
mcdonalds.delivery = True

north_fish = Restaurant()
north_fish.name = 'North Fish'
north_fish.category = 'Seafood'
north_fish.rating = 4.3
north_fish.delivery = False

print(vars(bobs_burgers))
print(vars(mcdonalds))
print(vars(north_fish))