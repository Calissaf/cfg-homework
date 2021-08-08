#I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
# Write a program to calculate this.
# Assume that a box of eggs contains six eggs
# I need four eggs for each omelette
# I should be able to easily change these values if I want.
# The output should say something like:
# "You can make 9 omelettes with 6 boxes of eggs".
import math

eggs_per_box = 8
eggs_per_omelette = 4
number_of_boxes = 5
eggs_in_fridge = eggs_per_box * number_of_boxes

number_of_omelettes = math.floor(eggs_in_fridge / eggs_per_omelette)
eggs_remaining = eggs_in_fridge % eggs_per_omelette

message = 'You can make {} omelettes with {} boxes of eggs and have {} eggs leftover'.format(number_of_omelettes, number_of_boxes, eggs_remaining)

print(message)