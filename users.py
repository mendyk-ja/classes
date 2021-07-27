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
        print(f"Fist name: {self.first_name}"
              f"Last name: {self.last_name}"
              f"Age: {self.age}"
              f"Country: {self.country}")

    def greet_user(self):
        """Method for greeting users"""
        print(f"Hello, {self.first_name}! Glad to see you again!")


first_one = User('thomas', 'smith', 18,  'USA')
first_one.describe_user()
first_one.greet_user()

second_one = User('luca' 'lampariello', 35, 'italy')
second_one.describe_user()
second_one.greet_user()

third_one = User('steve', 'kaufmann', 70, 'USA')
third_one.describe_user()
third_one.greet_user()
