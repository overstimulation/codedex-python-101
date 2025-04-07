class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

warsaw = City(
    name="Warsaw",
    country="Poland",
    population=1860000,
    landmarks=['Old Town', 'Royal Castle', 'Palace of Culture and Science']
)

tokyo = City(
    name="Tokyo",
    country="Japan",
    population=14000000,
    landmarks=['Tokyo Skytree', 'Shibuya Crossing', 'Mount Fuji']
)

print(vars(warsaw))
print(vars(tokyo))