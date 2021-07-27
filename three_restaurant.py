class Restaurant:
    """Just simple representation of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is the best restaurant with {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open 14-22")


first_restaurant = Restaurant('boski schabowy', 'polish')
first_restaurant.describe_restaurant()

second_restaurant = Restaurant('ustafar', 'malaysian')
second_restaurant.describe_restaurant()

third_restaurant = Restaurant('babrakar', 'vietnamese')
third_restaurant.describe_restaurant()