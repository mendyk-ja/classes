class Restaurant:
    """Just simple representation of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{new_restaurant.restaurant_name.title()} is the best restaurant with {new_restaurant.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{new_restaurant.restaurant_name.title()} is open 14-22")


new_restaurant = Restaurant('khinkalnia', 'georgian')

print(f"This restaurant name is {new_restaurant.restaurant_name.title()}.")
print(f"This restaurant served {new_restaurant.cuisine_type} cuisine.")

