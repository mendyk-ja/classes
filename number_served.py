class Restaurant:
    """Just simple representation of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is the best restaurant with {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open 14-22")

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, additional_clients):
        self.number_served += additional_clients


new_restaurant = Restaurant('khinkalnia', 'georgian')
new_restaurant.number_served = 30

new_restaurant.set_number_served(15)
new_restaurant.set_number_served(134)

new_restaurant.increment_number_served(5)
new_restaurant.increment_number_served(7)
new_restaurant.increment_number_served(1)


print(f"Number of client served: {new_restaurant.number_served}")
