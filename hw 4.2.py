# I'm setting up my own market stall to sell chocolates.
# I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices.
# Finish the program by asking the user to input an item and then output its price.

chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

chocolate_request = input('What type of chocolate would you like? ').lower()

if chocolate_request in chocolates:
    print('{} chocolate costs £{}'.format(chocolate_request, chocolates[chocolate_request]))
else:
    print('Chocolate not recognised please try another type')