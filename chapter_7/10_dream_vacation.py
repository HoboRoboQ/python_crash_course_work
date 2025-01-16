prompt = "If you could visit one place in the world, where would you go?"

locations = {}

poll = True
while poll:
    name = input("What is your name?:\n")
    place = input("Where would you like to go?:\n")
    locations[name] = place

    repeat = input("Would anyone else like to take the poll? (yes / no): ")

    if repeat == 'no':
        poll = False

print("--- Poll Results ---")
for name, place in locations.items():
    print(f"{name.title()} would like to go to {place.title()}.")