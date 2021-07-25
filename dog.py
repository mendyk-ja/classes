class Dog():
    """Simple class for representing model of dog"""

    def __init__(self, name, age):
        """Initialization attributes name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulation that dog sits after taking a command"""
        print(f"{self.name.title()} is sitting now")

    def roll_over(self):
        """Simulation that dog lays on his back after taking a command"""
        print(f"{self.name.title()} is  lying on his back now")