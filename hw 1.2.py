#I'm trying to run this program, but I get an error.
# What is the error telling me is wrong? How do I fix the program?
# my_name = Penelope
# my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)

#ANSWER: my_name is set to a variable that isn't given quotation marks to classify it as a string therefore complier thinks it is another variable
#Correct code below:

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)