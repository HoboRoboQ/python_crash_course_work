pets = []

# Generate pets and owners.
pet = {
    'animal' : 'dog',
    'name' : 'finlay',
    'owner' : 'fran',
    'age' : 1.5,
}
pets.append(pet)

pet = {
    'animal' : 'ferret',
    'name' : 'bean',
    'owner' : 'thor',
    'age' : 3,
}
pets.append(pet)

pet = {
    'animal' : 'dog',
    'name' : 'scooby doo',
    'owner' : 'shaggy',
    'age' : 25,
}
pets.append(pet)

for pet in pets:
    animal = pet['animal']
    name = pet['name'].title()
    owner = pet['owner'].title()
    age = pet['age']
    print(f"{owner.title()}'s {animal}, {name.title()}, is {age} years old.")
