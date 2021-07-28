class Car:
    """Simple car representation trial"""

    def __init__(self, make, model, year):
        """Initialization attributes describing a car"""
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


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()