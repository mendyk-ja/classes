from random import choice

"""Piece of code, which draw a random number or letter from list my_list"""
my_list = ['a', 'b', 'c ', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(f"Lottery wins a person, who has that number or letter: {choice(my_list)}")

"""This piece of code is checking how many times you would needed to draw to win the lottery."""
lottery_number = None 
my_number = choice(my_list)
my_ticket = []
number_of_draw = 0
while lottery_number != my_number:
    lottery_number = choice(my_list)
    number_of_draw += 1
print(f"You would won after {number_of_draw} times draw.")

