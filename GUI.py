"""Gui van de applicatie"""

# import functionaliteit van main.py en packages
from main import *
from tkinter import *
from steamFunctions import *

# Tkinter setup settings:
root = Tk()
root.geometry('1024x720')
root.title('Steam App Fantastic Five')
root['bg'] = '#393D47'
root.wait_visibility(root)
root.wm_attributes('-alpha', 0.9)


# De labels die je ziet op scherm

# Label van eerste spel in lijst:
L1 = Label(root, text="First game in list:", background='#393D47', foreground='white').grid(column=1, row=1)
L2 = Label(root, text=first_game_in_json, background='yellow', foreground='black').grid(column=2, row=1)

# label van gemiddelde prijs van de games:
L3 = Label(root, text="Average game price:", background='#393D47', foreground='white').grid(column=1, row=2)
L4 = Label(root, text=average_game_price(), background='yellow', foreground='black').grid(column=2, row=2)

# Label van eerste game dev in de lijst":
L5 = Label(root, text="First game developer:", background='#393D47', foreground='white').grid(column=1, row=3)
L6 = Label(root, text=list_first_game_developers(), background='yellow', foreground='black').grid(column=2, row=3)

# Knop om programma te eindigen
B1 = Button(root, text="Quit Steam Dashboard", command=root.destroy).grid(column=1, row=4)

# Run het programma
root.mainloop()