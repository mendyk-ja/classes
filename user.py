"""Class, which will be used to represent an user"""


class User:
    """Simple representation of user"""

    def __init__(self,  first_name, last_name, age, country, ):
        """Initialization attributes first_name, last_name, age  and country"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """Method which prints data about user"""
        print(f"Fist name: {self.first_name.title()}; "
              f"Last name: {self.last_name.title()}; "
              f"Age: {self.age}; "
              f"Country: {self.country.title()}.")

    def greet_user(self):
        """Method for greeting users"""
        print(f"Hello, {self.first_name}! Glad to see you again!")
