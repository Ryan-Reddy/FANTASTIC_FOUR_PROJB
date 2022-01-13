"""Gui van de applicatie"""

from main import *
from tkinter import *
import tkinter.ttk as ttk
from steamFunctions import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tkinter kleurkeuzes ***Alleen deze wijzigen!***:
back_color = '#393D47'
font_color = 'white'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Mainscreen GUI settings:
root = Tk()
# Raam formaat:
root.geometry('1024x720')
# title naam:
root.title('Steam App Fantastic Five')
# Achtergrond kleur:
root['bg'] = back_color
# Wacht totdat de pagina zichtbaar is, en maakt dan pagina doorzichtig 90%
root.wait_visibility(root)
root.wm_attributes('-alpha', 0.9)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Readme scherm GUI:
def openNewWindow_readme():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    # sets the geometry of toplevel
    newWindow.geometry('1024x720')
    # Achtergrond kleur van de readme
    newWindow['bg'] = back_color
    # A Label widget to show in toplevel
    Label(newWindow, fg=font_color, bg=back_color, text=get_readme()).pack()
    B3 = Button(newWindow, text="Back ", command=newWindow.destroy).pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# De labels die je ziet op scherm
# Label van eerste spel in lijst:
L1 = Label(root, text="First game in list:", background=back_color, foreground=font_color).grid(column=1, row=1)
L2 = Label(root, text=first_game_in_json, background='yellow', foreground='black').grid(column=2, row=1)

# label van gemiddelde prijs van de games:
L3 = Label(root, text="Average game price:", background=back_color, foreground=font_color).grid(column=1, row=2)
L4 = Label(root, text=average_game_price(), background='yellow', foreground='black').grid(column=2, row=2)

# Label van eerste game dev in de lijst:
L5 = Label(root, text="First game developer:", background=back_color, foreground=font_color).grid(column=1, row=3)
L6 = Label(root, text=list_first_game_developers(), background='yellow', foreground='black').grid(column=2, row=3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Knop om programma te eindigen
B1 = Button(root, text="Quit Steam Dashboard", command=root.destroy).grid(column=1, row=4)

# Knop voor about
B2 = Button(root, text="About", command=openNewWindow_readme).grid(column=2, row=4)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(root,bd=0,bg=back_color, sashwidth=2)
separator.grid(column=2, row=5)
# rechter onderhoekje:
_frame = Frame(root,bg="#383838")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Treeview columns instellen
treeview = ttk.Treeview(root, show="headings", columns=("Name", "Developer", "Platforms"))
treeview.heading("#1", text="Name")
treeview.heading("#2", text="Developer")
treeview.heading("#3", text="Platforms")
treeview.grid()

# Plaatst data van data_import(main) in treeview tabel
for row in data_import:
    treeview.insert("", "end", values=(row["name"], row["developer"], row["platforms"]))

ysb = ttk.Scrollbar(orient=VERTICAL, command= treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command= treeview.xview)
treeview['yscroll'] = ysb.set
treeview['xscroll'] = xsb.set

ttk.Style().configure(treeview, background="#383838",foreground="white")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
ysb.grid(in_=_frame, row=0, column=1, sticky=NS)
xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
_frame.rowconfigure(0, weight=1)
_frame.columnconfigure(0, weight=1)

separator.add(_frame)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Run het programma
root.mainloop()