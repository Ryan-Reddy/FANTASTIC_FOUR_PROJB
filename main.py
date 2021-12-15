# Imported Packages:
import json
from tkinter import *

# Functions:
def startup_message():
    print('hello worlrld'.format())
    num = sum(1 for element in open('steam.json'))
    print('steam.json contains: ', num, ' records,')

    stream = open('steam.json', 'r')
    steam = stream.read()
    print('divided over ',len(steam), ' lines.')

def get_gamename(steamy):
    return steamy.get('name')


f = open('steam.json')
data = json.load(f)
data_import = []
for line in data:
    data_import.append(line)

# return first_game_in_json
first_game_in_json = data_import[0]['name']

print(data_import[0]['name'])

# sort by gamename, print top
data_import.sort(key=get_gamename)
print('yes', data_import[0]['name'])

# reverse sort by gamename, print top
data_import.sort(key=get_gamename, reverse=True)
print('yes', data_import[0]['name'])



# Main Program:
startup_message()
