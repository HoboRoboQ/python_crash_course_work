cities = {
    'santiago' : {
        'country' : 'chile',
        'population' : 6_300_000,
        'nearby_mountains' : 'andes',
    },
    'talkeetna' : {
        'country' : 'united states',
        'population' : 876,
        'nearby_mountains' : 'alaska range',
    },
    'kathmandu' : {
        'country' : 'nepal',
        'population' : 975_453,
        'nearby_mountains' : 'himilaya',
    },
}

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['nearby_mountains'].title()
    
    print(f"{city.title()} is in {country.title()}.")
    print(f"It has a population of {population}.")
    print(f"The {fact} mountains are nearby.\n")