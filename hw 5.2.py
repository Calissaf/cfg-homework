#This program should save my data to a file,
# but it doesn't work when I run it.
# What is the problem and how do I fix it?
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'r') as poem_file:
# poem_file.write(poem)

#ANSWER:
# File is opened in read format so unable to save changes
# Change opening type to write+ to save changes to the file

poem = 'I like Python and I am not very good at poems'

with open('poem.txt', 'w+') as poem_file:
    poem_file.write(poem)
   