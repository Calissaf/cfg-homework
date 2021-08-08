#I have a list of things I need to buy from my supermarket of choice.
#shopping_list = [
# "oranges", "cat food", "sponge cake", "long-grain rice", "cheese board",
#]
#print(shopping_list[1])
#I want to know what the first thing I need to buy is.
# However, when I run the program it shows me a different answer to what I was expecting?
#What is the mistake? How do I fix it?

#ANSWER: The code requests the 1 index item in the list
# indexes start from 0 so to pull the first item in the list
# need to print the 0 index
#CORRECT CODE:
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake", 
    "long-grain rice",
    "cheese board",
]

print(shopping_list[0])