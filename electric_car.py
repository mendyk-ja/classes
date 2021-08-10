"""Set of class intended for representation of electric car"""

from car import Car


class Battery:
    """Simple trial to model battery of electric car"""

    def __init__(self, battery_size=75):
        """Initialization of battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Displaying information about battery size"""
        print(f"This car's battery has size of {self.battery_size} kWh.")

    def get_range(self):
        """
        Displays information about car's range based on battery's capacity
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Range of this car is more or less {range} km with full charged battery.")

    def upgrade_battery(self):

        if self.battery_size < 100:
            self.battery_size = 100

        print("Your battery has been upgraded to 100 kWh.")


class ElectricCar(Car):
    """Represent characteristics of electric car."""

    def __init__(self, make, model, year):
        """
        Initialization attributes of main class.
        Then representation of electric car's characteristic attributes.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


