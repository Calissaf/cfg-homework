#'m on holiday and want to hire a boat.
# The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
#Have a look at my program and work out what I've done wrong:
#my_money = input('How much money do you have? ')
#boatcost=20+5
#if my_money < boat_cost:
#print('You can afford the boat hire')
#else:
#print('You cannot afford the board hire')
#ANSWER: 1) input is not a float, if statement compares a string and an int which is invalid
#ANSWER: 2) if statment uses boat_cost but variable is labelled boat cost
#ANWSER: 3) greater than symbol is wrong way round (you should have more money than boat_cost)
#ANSWER:
my_money = float(input('How much money do you have? '))
boat_cost = 20+5

if my_money > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')