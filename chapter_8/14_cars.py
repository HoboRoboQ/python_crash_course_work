# def car_info(manufacturer, model_name, **car_profile):
#     """Create dictionary about car information"""
#     car_profile['manufacturer'] = manufacturer
#     car_profile['model'] = model_name
#     return car_profile

# car = car_info('subaru', 'outback', color='blue', tow_package='True')
# print(car)

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)