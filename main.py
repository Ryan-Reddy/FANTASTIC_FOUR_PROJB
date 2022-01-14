# Imported Packages:
import json
import glob


# Functions:
def startup_message():
    print('Starting up programme...'.format())

    # count records in list:
    num = sum(1 for element in open('steam_small.json'))

    # print amount datapoints
    print('steam_small.json contains: ', num, ' records,')

    # read and count lines:
    stream = open('steam_small.json', 'r')
    steam = stream.read()
    print('divided over ', len(steam), ' lines.')


def get_readme():
    all_readmes = glob.glob("README.md")
    # return first readme in list
    return open(all_readmes[0], 'r', encoding='utf-8').read()




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Mainscreen functions:

def get_gamename(steamy):
    return steamy.get('name')


# Laadt het .json bestand in een list
f = open('steam_small.json')
data = json.load(f)
data_import = []
for line in data:
    data_import.append(line)

# return first_game_in_json
first_game_in_json = data_import[0]['name']
print(data_import[0]['name'])

# sort by gamename, print top
data_import.sort(key=get_gamename)
print('first game in list', data_import[0]['name'])

# reverse sort by gamename, print top, then resort list (normal)
data_import.sort(key=get_gamename, reverse=True)
print('last game in list', data_import[0]['name'])
# reverse to normal
data_import.sort(key=get_gamename)

# Main Program:
startup_message()
