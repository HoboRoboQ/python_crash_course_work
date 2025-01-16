favorite_places = {
    'fran' : ['monmarte', 'shirakawago', 'akihabara'],
    'meg' : ['akihabara', 'barbatos', 'home'],
    'nat' : ['akihabara', 'barbatos', 'home'],
    'mayumi' : ['home', 'madrid', 'tokyo'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")