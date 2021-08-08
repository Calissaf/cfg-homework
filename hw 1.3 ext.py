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
number_of_omelettes = 9

boxes_needed = math.ceil((eggs_per_omelette * number_of_omelettes) / eggs_per_box)
eggs_remaining = (boxes_needed * eggs_per_box) - (eggs_per_omelette * number_of_omelettes)

message = 'You can make {} omelettes with {} boxes of eggs with {} eggs leftover'.format(number_of_omelettes, boxes_needed, eggs_remaining)

print(message)