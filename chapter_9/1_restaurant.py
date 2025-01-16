class Restaurant:
    """Model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Creates description of restaurant."""
        print(f"The name of this restaurant is {self.restaurant_name}.")
        print(f"It is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """Indicates restaurant is open."""
        print("The restaurant is open.")

restaurant_a = Restaurant('Ootoya', 'Japanese')
restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()

restaurant_b = Restaurant('Bonjour', 'French')
restaurant_b.describe_restaurant()

restaurant_c = Restaurant('Ganesha', 'Nepali')
restaurant_c.describe_restaurant()