"""Gui van de applicatie"""

from main import *
from tkinter import *
import tkinter.ttk as ttk
from steamFunctions import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tkinter kleurkeuzes ***Alleen deze wijzigen!***:
back_color = 'black'
font_color = 'white'
font_choice = ('Helvetica', 12)
transparency = 0.75
# main_GUI_size
raam_formaat = '1024x420'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Mainscreen GUI settings:
root = Tk()
# Raam formaat:
root.geometry(raam_formaat)
# title naam:
root.title('Steam App Fantastic Five')
# Achtergrond kleur:
root['bg'] = back_color
# Wacht totdat de pagina zichtbaar is, en maakt dan pagina doorzichtig 90%
root.wait_visibility(root)
root.wm_attributes('-alpha', transparency)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Readme scherm GUI:
def open_new_window_readme():
    # Open as a new window
    new_window = Toplevel(root)

    # sets the title readme
    new_window.title("READ ME PLEASE")

    # sets the geometry of readme
    # new_window.geometry('1024x768')
    # new_window.resizable(False, False)



    # Achtergrond kleur van de readme
    new_window['bg'] = back_color
    new_window.wait_visibility(new_window)
    new_window.wm_attributes('-alpha', .99)

    # De data van de README.MD
    text = Text(new_window, width=120, height=40, font='TkFixedFont', fg=font_color, bg=back_color,)
    # plaatsen van grid (moet apart anders herkent de scrollbar m niet
    text.grid(row=0)
    text.insert(END, get_readme())

    # Scrollbar
    scrollbar = ttk.Scrollbar(new_window, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    # scrollbar style
    style = ttk.Style()
    style.theme_use('classic')
    style.configure("Vertical.TScrollbar", background="black", bordercolor="black", arrowcolor="white")

    # knop sluit de newwindow af
    Button(new_window, text="Back", bg='red', command=new_window.destroy).grid(row=1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# De labels die je ziet op scherm

# Label van eerste spel in lijst:
Label(root, text="First game in list:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=1, row=1)
Label(root, text=first_game_in_json, font=font_choice, background='yellow',
      foreground='black').grid(column=2, row=1)

# label van gemiddelde prijs van de games:
Label(root, text="Average game price:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=1, row=2)
Label(root, text=average_game_price(), font=font_choice, background='yellow',
      foreground='black').grid(column=2, row=2)

# Label van eerste game dev in de lijst:
Label(root, text="First game developer:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=1, row=3)
Label(root, text=list_first_game_developers(), font=font_choice, background='yellow',
      foreground='black').grid(column=2, row=3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Knoppen in mainscreen
# Knop om hoofdprogramma te eindigen
Button(root, text="Quit Steam Dashboard", font=font_choice, background='red', foreground=font_color,
       command=root.destroy).grid(column=1, row=4)

# Knop voor about(readme.md) in een apart scherm
Button(root, text="About", font=font_choice, background='gray', foreground=font_color,
       command=open_new_window_readme()).grid(column=2, row=4)

# knop om te sorteren

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(root, bd=0, bg=back_color, sashwidth=2)
separator.grid(column=2, row=5)
# rechter onderhoekje:
_frame = Frame(root, background=back_color, relief='ridge')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Geeft aan welke data uit de dictionairy mee te nemen
treeview = ttk.Treeview(root, show="headings",
                        columns=("Name", "Developer", "Platforms", "Genre"))

# Voegt Kolomkoppen toe
treeview.heading("#1", text="Name")
treeview.heading("#2", text="Developer")
treeview.heading("#3", text="Platforms")
treeview.heading("#4", text="Genre")

# Plaatst data van data_import(main) in treeview tabel
for row in data_import:
    treeview.insert("", "end", values=(row["name"], row["developer"], row["platforms"], row["genres"]))

# SCROLLBAR van tabel
ysb = ttk.Scrollbar(orient=VERTICAL, command=treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command=treeview.xview)
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
