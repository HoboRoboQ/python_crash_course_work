fav_number = {
    'ryan' : [23, 42],
    'mayumi' : [5, 15, 30],
    'nat' : [10, 2, 26],
    'fran' : [13, 4],
    'carlos' : [5, 100, 25],
}

for name, numbers in fav_number.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t- {number}")
