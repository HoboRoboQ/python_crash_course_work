people = []

# Generate/define people and put in list
person = {
    'first' : 'ryan',
    'last' : 'thomas',
    'age' : 33,
    'city' : 'cincinnati',
}
people.append(person)

person = {
    'first' : 'fran',
    'last' : 'valcarcel',
    'age' : 29,
    'city' : 'miami',
}
people.append(person)

person = {
    'first' : 'nat',
    'last' : 'torchia',
    'age' : 35,
    'city' : 'endmonton',
}
people.append(person)

for person in people:
    name = f"{person['first'].title()} {person['last'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")