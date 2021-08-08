# In this session you used the Pokemon API to retrieve a single Pokemon.
# I want a program that can retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs.
# Then in a for loop call the API to retrieve the data for each Pokemon.
# Save their names and moves into a file called 'pokemon.txt'

import requests

number_of_IDs = 6
pokemon_IDs = []


for ID in range(number_of_IDs):
    ID_number = int(input('Pick an ID number: '))
    pokemon_IDs.append(ID_number)


def get_pokeon(pokemon_ID, data):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_ID)
    response = requests.get(url)
    pokemon = response.json()
    return pokemon[data]

with open('pokemon.txt', 'w+') as pokemon_file:
    for ID in range(number_of_IDs):
        pokemon_file.write(get_pokeon(pokemon_IDs[ID], 'name') + '\n')
        moves = get_pokeon(pokemon_IDs[ID], 'moves')
        for move in moves:
            pokemon_file.write(move['move']['name'] + '\n')
        pokemon_file.write('\n')

