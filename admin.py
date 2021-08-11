"""Class, which will be used to represent an admin"""
from user import User
from privileges import Privileges


class Admin(User):

    def __init__(self,  first_name, last_name, age, country, ):
        """Initialization attributes first_name, last_name, age  and country"""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(('can add post', 'can delete post', 'can ban users'))
