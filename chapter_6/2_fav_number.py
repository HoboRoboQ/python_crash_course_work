fav_number = {
    'ryan' : 23,
    'mayumi' : 5,
    'nat' : 10,
    'fran' : 13,
    'carlos' : 5,
}

#print(fav_number['carlos'])
#print(fav_number['ryan'])
#print(fav_number['mayumi'])
#print(fav_number['nat'])
#print(fav_number['fran'])

# Loops the combination of keys and values
for name, number in fav_number.items():
    print(f"{name.title()}'s favorite number is {number}.")

# Loops the keys in a dictionary
for name in fav_number.keys():
    print(name.title())

# Loops through the values
friends = ['ryan', 'fran',]
for name in fav_number.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        number = fav_number[name]
        print(f"\t{name.title()}, I see you like {number}")


for name in sorted(fav_number.keys()):
    print(f"Thank you {name.title()} for taking the poll.")

for number in set(fav_number.values()):
    print(number)