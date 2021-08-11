from random import randint


class Dice:
    """Representation of dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


my_dice = Dice()

my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
