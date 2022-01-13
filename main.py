# Imported Packages:
import json
import glob

# Functions:
def startup_message():
    print('Starting up programme...'.format())

    # count records in list:
    num = sum(1 for element in open('steam.json'))

    # print amount datapoints
    print('steam.json contains: ', num, ' records,')

    # read and count lines:
    stream = open('steam.json', 'r')
    steam = stream.read()
    print('divided over ',len(steam), ' lines.')


def get_readme():
    """Get the README from the current directory.

    **Args:**
        None

    **Returns:**
        str:    String is empty if no README file exists.
    """
    all_readmes = sorted(glob.glob("README*"))
    if len(all_readmes) > 1:
        warnings.warn(
            "There seems to be more than one README in this directory."
            "Choosing the first in lexicographic order."
        )
    if len(all_readmes) > 0:
        return open(all_readmes[0], 'r').read()

    warnings.warn("There doesn't seem to be a README in this directory.")
    return ""


def get_gamename(steamy):
    return steamy.get('name')


# Laadt het .json bestand in een list
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
print('first game in list', data_import[0]['name'])

# reverse sort by gamename, print top, then resort list (normal)
data_import.sort(key=get_gamename, reverse=True)
print('last game in list', data_import[0]['name'])
#
data_import.sort(key=get_gamename)


# Main Program:
startup_message()
