#Explain what this program does
#for number in range(100):
#   output = 'o' * number
#   print(output)

#ANSWER:
#This program prints out 99 lines of o's starting with 1 o
#Incrementing the number of o's printed by 1 each line
#Technically prints 100 lines however starts at 0 and 0 * 'o' = 0 so no text is printed

for number in range(100):
   output = 'o' * number
   print(output)