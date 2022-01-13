"""Gui van de applicatie"""

from main import *
from tkinter import *
import tkinter.ttk as ttk
from steamFunctions import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tkinter kleurkeuzes ***Alleen deze wijzigen!***:
back_color = '#393D47'
font_color = 'white'
font_choice =('Helvetica', 12)

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
root.wm_attributes('-alpha', 0.8)

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
    # De data van de README.MD
    Label(newWindow, fg=font_color, bg=back_color, text=get_readme()).pack()
    B3 = Button(newWindow, text="Back ", command=newWindow.destroy).pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# De labels die je ziet op scherm
# Label van eerste spel in lijst:
L1 = Label(root, text="First game in list:", font=font_choice, background=back_color, foreground=font_color).grid(column=1, row=1)
L2 = Label(root, text=first_game_in_json, font=font_choice, background='yellow', foreground='black').grid(column=2, row=1)

# label van gemiddelde prijs van de games:
L3 = Label(root, text="Average game price:", font=font_choice, background=back_color, foreground=font_color).grid(column=1, row=2)
L4 = Label(root, text=average_game_price(), font=font_choice, background='yellow', foreground='black').grid(column=2, row=2)

# Label van eerste game dev in de lijst:
L5 = Label(root, text="First game developer:",font=font_choice, background=back_color, foreground=font_color).grid(column=1, row=3)
L6 = Label(root, text=list_first_game_developers(), font=font_choice, background='yellow', foreground='black').grid(column=2, row=3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Knop om programma te eindigen
B1 = Button(root, text="Quit Steam Dashboard", font=font_choice, background='red', foreground=font_color,
            command=root.destroy).grid(column=1, row=4)

# Knop voor about
B2 = Button(root, text="About", font=font_choice, background='gray', foreground=font_color,
            command=openNewWindow_readme).grid(column=2, row=4)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(root,bd=0,bg=back_color, sashwidth=2)
separator.grid(column=2, row=5)
# rechter onderhoekje:
_frame = Frame(root,background=back_color, relief='ridge')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Geeft aan welke data uit de dictionairy mee te nemen
treeview = ttk.Treeview(root, show="headings", columns=("Name", "Developer", "Platforms", "Genre"), style="TVmystyle.Treeview")

# Voegt Kolomkoppen toe
treeview.heading("#1", text="Name")
treeview.heading("#2", text="Developer")
treeview.heading("#3", text="Platforms")
treeview.heading("#4", text="Genre")

# Plaatst data van data_import(main) in treeview tabel
for row in data_import:
    treeview.insert("", "end", values=(row["name"], row["developer"], row["platforms"], row["genres"]))

# SCROLLBAR van tabel
ysb = ttk.Scrollbar(orient=VERTICAL, command= treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command= treeview.xview)
treeview['yscroll'] = ysb.set
treeview['xscroll'] = xsb.set
separator.add(_frame)

# Geeft de stijl van de tabel aan
ttk.Style().configure("treeview", font=font_choice, background=back_color, foreground=font_color, fieldbackground="red")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Geeft aan waar de tabel in het grid moet
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)

# plaatst de scrollbar
ysb.grid(in_=_frame, row=0, column=1, sticky=NS)
xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
_frame.rowconfigure(0, weight=1)
_frame.columnconfigure(0, weight=1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Run het programma
root.mainloop()
