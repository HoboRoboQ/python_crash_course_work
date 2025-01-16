def describe_city(city, country='the United States'):
    """Describes a city and country of location."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('los angeles')
describe_city('miami')
describe_city('tokyo', country='japan')