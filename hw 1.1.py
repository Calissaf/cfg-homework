#I am building some very high quality chairs and need exactly four nails for each chair. I've written a program to calculate how many nails I need to buy to build these chairs.
# chairs = '15'
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message))
# When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails.
# Is my program calculating the total number of nails correctly? What is the problem? How do I fix it?

#ANSWER: The code multplies a string and an interger together
# ANSWER pt2: the variable message has script in it that is repeated in print statement
# resulting in: "You need to buy I need to buy 60 nails nails"
# correct code below:

chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)