class Car:
    """Simple car representation trial"""

    def __init__(self, make, model, year):
        """Initialization of attributes describing a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Output of elegantly formatted description"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Displaying information obout car's mileage"""
        print(f"This car has driven {self.odometer_reading} miles.")

    def update_odometer(self, mileage):
        """
        Assignment of nev value to a car's odometer.
        Assignment will be rejected in case of making odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't make a car's odometer back!")

    def increment_odometer(self, miles):
        """Incrementation of odometer's value by a given value"""
        self.odometer_reading += miles


class Battery:
    """Simple trial to model battery of electric car"""

    def __init__(self, battery_size=75):
        """Initialization of battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Displaying information about battery size"""
        print(f"This car's battery has size of {self.battery_size} kWh")

    def get_range(self):
        """
        Displays information about car's range based on battery's capacity
        """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Range of this car is more or less {range} km with full charged battery")


class ElectricCar(Car):
    """Represent characteristics of electric car."""

    def __init__(self, make, model, year):
        """
        Initialization attributes of main class.
        Then representation of electric car's characteristic attributes.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

