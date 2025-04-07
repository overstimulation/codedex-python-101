class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    
    def speak(self):
        print(f'{self.name} {self.name}!')

    def display_details(self):
        print(f'Entry Number: {self.entry}')
        print(f'Name: {self.name}')
        print(f'Type: {self.types}')
        print(f'Description: {self.description}')
        if self.is_caught:
            print(f'{self.name} has already been caught!')
        else:
            print(f'{self.name} has not been caught yet!')

jigglypuff = Pokemon(
    39,
    'Jigglypuff',
    ['Normal', 'Fairy'],
    'When its huge eyes waver, it sings a mysteriously soothing melody that lulls its enemies to sleep.',
    True
)

hypno = Pokemon(
    97,
    'Hypno',
    ['Psychic'],
    'When it locks eyes with an enemy, it will use a mix of psi moves, such as Hypnosis and Confusion.',
    False
)

magikarp = Pokemon(
    129,
    'Magikarp',
    ['Water'],
    'An underpowered, pathetic Pokémon. It may jump high on rare occasions but never more than seven feet.',
    True
)

jigglypuff.speak()
jigglypuff.display_details()
hypno.speak()
hypno.display_details()
magikarp.speak()
magikarp.display_details()