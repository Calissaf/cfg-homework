# Write a program that simulates a lottery.
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers
import random

ticket_length = 7

winnings = {
    3: 20,
    4: 40,
    5: 100,
    6: 10000,
    7: 1000000
}

def random_ticket_generator(input_func):
    ticket = []
    number = input_func()

    for choice in range(ticket_length):
        while number in ticket:
            number = input_func()
        ticket.append(number)
    return ticket


def get_user_input():
    pick_number = int(input('Please pick a number between 1 and 10 '))
    while pick_number not in range(1, 10):
        pick_number = int(input('Number out of range. Please pick a number between 1 and 10  '))
    return pick_number


def get_random_input():
    return random.randint(1, 10)

def matches(lottery_results, user_ticket):
    counter = 0
    for user_choice in range(ticket_length):
        if user_ticket[user_choice] in lottery_results:
            counter = counter + 1
    return counter


user_ticket = random_ticket_generator(get_user_input)
lottery_results = random_ticket_generator(get_random_input)
ticket_match = matches(lottery_results, user_ticket)


print('Your ticket {}'.format(user_ticket))
print('results {}'.format(lottery_results))
print('matches {}'.format(ticket_match))

if ticket_match in winnings:
    print('congratulations you have won £{}'.format(winnings[ticket_match]))