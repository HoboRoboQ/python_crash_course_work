class Restaurant:
    """Model of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
        
    def describe_restaurant(self):
        """Creates description of restaurant."""
        print(f"\nThe name of this restaurant is {self.restaurant_name}.")
        print(f"It is a {self.cuisine_type} restaurant.")
    
    def open_restaurant(self):
        """Indicates restaurant is open."""
        print("The restaurant is open.")
    
    def set_number_served(self, number_served):
        """Set the number of customers served"""
        self.number_served = number_served
    
    def increase_number_served(self, increase):
        """Lets user increase the number served."""
        self.number_served += increase

class IceCreamStand(Restaurant):
    """Model of ice cream stand that inherits from Restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize aspects of parent and ice cream stand."""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display flavors available."""

        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

scoops = IceCreamStand('scoops')
scoops.flavors = ['vanilla', 'chocolate', 'black cherry']

scoops.describe_restaurant()
scoops.show_flavors()