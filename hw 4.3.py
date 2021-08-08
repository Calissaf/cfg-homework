#Write a program that simulates a lottery.
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based on the number of matches:
#● £20 for three matching numbers
#● £40 for four matching numbers
#● £100 for five matching numbers
#● £10000 for six matching numbers
#● £1000000 for seven matching numbers
import random
ticket_length = 7

def random_ticket():
    ticket = []
    random_choice = random.randint(1,10)
    # range to 59 for lottery odds
    for choice in range(ticket_length):
        while random_choice in ticket:
            random_choice = random.randint(1, 10)
            # makes sure all numbers picked are unique
        ticket.append(random_choice)
    return ticket

#NO USER INPUT:
#ticket = random_ticket()
results = random_ticket()
counter = 0

#USER INPUT:
ticket = []

for number in range(ticket_length):
    pick_number = int(input('Please pick a number between 1 and 10 '))
    while pick_number not in range(1,10) or pick_number in ticket:
        pick_number = int(input('Please pick another number between 1 and 10 '))
    ticket.append(pick_number)

print('Your ticket {}'.format(ticket))

winnings = {
    3: 20,
    4: 40,
    5: 100,
    6: 10000,
    7: 1000000
}

for choice in range(ticket_length):
    if ticket[choice] in results:
        counter = counter + 1

print('results {}'.format(results))
print('matches {}'.format(counter))

if counter in winnings:
    print('congratulations you have won £{}'.format(winnings[counter]))