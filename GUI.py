"""Gui van de applicatie"""
from main import *
from tkinter import *

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