def city_country(city, country):
    """Return a city and country."""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('long beach', 'america')
print(city)

city = city_country('lima', 'peru')
print(city)  