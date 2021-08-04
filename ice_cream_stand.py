class Restaurant:
    """Just simple representation of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is the best restaurant with {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open 14-22")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """"
        Initialization attributes of main class.
        Then representation of Ice Cream Stand's characteristic attributes.
        """
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = ['awful', 'nice', 'nothing special']

    def describe_flavours(self):
        print(f'Available flavours are: {self.flavours}.')


koral = IceCreamStand('koral', 'sweets')
koral.describe_flavours()

