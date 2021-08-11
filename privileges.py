"""Class, which will be used to represent privileges"""


class Privileges:
    """Representation of admin privileges"""

    def __init__(self, privileges=None):
        """Initialization of Privileges's attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """ Method for displaying privileges"""
        print(f"List of possible actions: {self.privileges}")
