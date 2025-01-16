from city_function import city_country

def test_city_country():
    """Do these city and country inputs work?"""
    place = city_country('santiago', 'chile')
    assert place == 'Santiago, Chile'

def test_city_country_population():
    """Do these city and country inputs work?"""
    place = city_country('santiago', 'chile', 5600000)
    assert place == 'Santiago, Chile - population 5600000'