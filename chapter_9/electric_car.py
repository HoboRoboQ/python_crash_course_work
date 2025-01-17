"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """A simple attempt too model a battery for an electric car."""

    def __init__ (self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
     """Represents aspects of car, specific to electric vehicles."""
    
     def __init__(self, make, model, year):
         """Initialize attributes of the parent class. Then initialize 
         attributes specific to an electric car."""
         super().__init__(make, model, year)
         self.battery = Battery()