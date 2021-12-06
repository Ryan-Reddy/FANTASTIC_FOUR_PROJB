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

def GUI_function():
    root = Tk()
    root.geometry('1024x720')
    root.title('Steam App Fantastic Five')
    root['bg'] = '#393D47'
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.9)

    L1 = Label(root, text="First game in list:", background='#393D47', foreground='white').grid(column=2, row=1)
    L2 = Label(root, text=first_game_in_json, background='yellow', foreground='black').grid(column=3, row=2)

    B1 = Button(root, text="Quit", command=root.destroy).grid(column=2, row=5)

    root.mainloop()


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
GUI_function()
