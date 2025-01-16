def city_country(city, country, population=''):
    """Produce set of city and country."""
    if population:
        place = f"{city.title()}, {country.title()} - population {population}"
    else:
        place = f"{city.title()}, {country.title()}"
    return place