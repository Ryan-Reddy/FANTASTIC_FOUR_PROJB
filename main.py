# Imported Packages:
import json
import glob

DATABASE_STEAM = "steam.json"


# Functions:
def startup_message():
    print("Starting up programme...".format())

    # count records in list:
    num = sum(1 for element in open(DATABASE_STEAM))  # <--- element not used

    # print amount datapoints
    print("steam.json contains: ", num, " records,")

    # read and count lines:
    stream = open(DATABASE_STEAM, "r")
    steam = stream.read()
    print("divided over ", len(steam), " lines.")


def get_readme():
    all_readmes = glob.glob("README.md")
    # return first readme in list
    return open(all_readmes[0], "r", encoding="utf-8").read()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Mainscreen functions:


def get_game(steamy):
    return steamy.get("name")

f = open(DATABASE_STEAM)
data_tree = json.load(f)
data_import = []
for line in data_tree:
    data_import.append(line)
# Laadt het .json bestand in een list
def first_game_in_json():

    f = open(DATABASE_STEAM)
    data_tree = json.load(f)
    data_import = []
    for line in data_tree:
        data_import.append(line)

    # return first_game_in_json
    print(data_import[0]["name"])
    first_game = data_import[0]["name"]
    print(first_game)
    return first_game


# sort by gamename, print top
data_import.sort(key=get_game)
print("first game in list", data_import[0]["name"])

# reverse sort by gamename, print top, then resort list (normal)
data_import.sort(key=get_game, reverse=True)
print("last game in list", data_import[0]["name"])
# reverse to normal
data_import.sort(key=get_game)

# Main Program:
startup_message()
