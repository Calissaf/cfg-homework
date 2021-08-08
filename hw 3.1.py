#Create a program that tells you whether or not you need an umbrella
# when you leave the house.
#The program should:
#1. Ask you if it is raining using input()
#2. If the input is 'y', it should output 'Take an umbrella'
#3. If the input is 'n', it should output 'You don't need an umbrella'
#ANSWER:

weather_outside = input('Is it raining outside? y/n ').lower()

if weather_outside == 'y':
    print('Take an umbrella')
elif weather_outside == 'n':
    print('You do not need an umbrella')
else:
    print('Please answer y or n')