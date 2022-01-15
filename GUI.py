"""GUI of the Application"""

import time
import random
from main import *
from tkinter import *
import tkinter.ttk as ttk
from steamFunctions import *
from PIL import Image, ImageTk

# ******************************************************************************************************************
# TODO add tkinter styles
"""#STYLE/COLOR CHOICES"""
# Tkinter kleurkeuzes ***Alleen deze wijzigen!***:
BACK_COLOR = "black"
FONT_COLOR = "white"
FONT_LOGO = ("FF Din OT", 14, "bold")  # <--- (STEAM_OFFICIAL)
FONT_MAIN = (
    "Arial" or "Helvetica",
    12,
)  # <--- Arial-standard, helvetica for MAC systems (STEAM_OFFICIAL)
TRANSPARENCY_BACKGROUND = 0.9  # <--- transparency mainscreen
FLAME_SPEED = 256
WINDOW_SIZE = ""  # <--- Autoadjusts to content
# ******************************************************************************************************************
# TODO: change changeable text at bottom to commits, last minute change
"""# SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme"""

splashscreen = Tk()  # <--- setup splashscreen
splashscreen.overrideredirect(True)  # <--- Removes TITELBALK

splashscreen.call("wm", "attributes", ".", "-topmost", "true")  # <--- # topmost screen

splashscreen.geometry(
    "960x307+471+387"
)  # <--- # size of screen + positie (steam-logo-large.jpg = 960x307)
splashscreen.geometry("")  # <--- autoadjust overrides upper geometry
# Achtergrond kleur van de readme (inclusief transparency)
splashscreen["bg"] = BACK_COLOR
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# load splashscreen picture order file:
with open(r"splashscreen\splash.txt") as splash_loader_filelist:
    print(splash_loader_filelist)
    splash_order = splash_loader_filelist.read().splitlines()
    splash_loader_filelist.close()
print(splash_order)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen IMAGER/motion sequence:


def change_label():
    for i in splash_order:
        splash_label.configure(
            text=i
        )  # <--- change bottom screen text each imagechange
        filename = i
        img_var = Image.open(filename)  # <--- load next image
        photo_image = ImageTk.PhotoImage(img_var)
        img_label.configure(image=photo_image)  # <--- swap current image with next
        splashscreen.update_idletasks()  # <--- run configure task while still in loop !!!!
        time.sleep(random.uniform(1, 2.2))


def delayed_start():
    change_label()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# initial fill splashscreen
img = Image.open(splash_order[0])
ph = ImageTk.PhotoImage(img)
img_label = Label(splashscreen, image=ph)
img_label.pack()
splash_label = Label(splashscreen, text="loading", bg=BACK_COLOR, fg="gold")
splash_label.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen programme:
splashscreen.after(
    12000, splashscreen.destroy
)  # ~12000ms set to 0 this one to skip splashscreen
# function should be "delayedstart":
splashscreen.after(2000, delayed_start)
splashscreen.after(0, print("starting splashscreen"))

splashscreen.mainloop()
# ******************************************************************************************************************
""" README SCREEN GUI:"""


def open_new_window_readme():
    new_window = Toplevel(root)  # <---     open new window
    new_window.title("READ ME PLEASE")  # <---     sets the title readme

    # Achtergrond kleur van de readme (inclusief transparency)
    new_window["bg"] = BACK_COLOR
    new_window.wait_visibility(new_window)
    new_window.wm_attributes("-alpha", 0.99)
    # De data van de README.MD
    text = Text(
        new_window,
        width=120,
        height=40,
        font="TkFixedFont",
        fg=FONT_COLOR,
        bg=BACK_COLOR,
    )
    # plaatsen van grid (moet apart anders herkent de scrollbar m niet)
    text.grid(row=0)
    text.insert(END, get_readme())

    # Scrollbar
    scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=text.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    # Readme scrollbar style
    my_style = ttk.Style()
    my_style.configure(
        "Vertical.TScrollbar",
        background="black",
        bordercolor="black",
        arrowcolor="white",
    )

    # knop sluit de newwindow af
    Button(new_window, text="Back", bg="red", command=new_window.destroy).grid(row=1)


# ******************************************************************************************************************
"""# MAIN-SCREEN ~ GUI settings:"""
root = Tk()
# Raam formaat:
root.geometry(WINDOW_SIZE)
# title naam:
root.title("Steam App Fantastic Five")
# Achtergrond kleur:
root["bg"] = BACK_COLOR
# Wacht totdat de pagina zichtbaar is, en maakt dan pagina doorzichtig 90%
root.wait_visibility(root)
root.wm_attributes("-alpha", TRANSPARENCY_BACKGROUND)
# ******************************************************************************************************************
"""# MAIN SCREEN ~ Labels and Buttons:"""

# De labels die je ziet op scherm
# TITEL
Label(
    root,
    text="Steam APP Fantastic Five",
    font=FONT_LOGO,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
    anchor=N,
    justify=CENTER,
).grid(column=1, row=0)

# Label van eerste spel in lijst:
Label(
    root,
    text="First game in list:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=1)
Label(
    root,
    text=first_game_in_json,
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=3, row=1)

# label van gemiddelde prijs van de games:
Label(
    root,
    text="Average game price:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=2)
Label(
    root,
    text=average_game_price(),
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=3, row=2)

# Label van eerste game dev in de lijst:
Label(
    root,
    text="First game developer:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=3)
Label(
    root,
    text=list_first_game_developers(),
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=3, row=3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Knoppen in mainscreen
# Knop om hoofdprogramma te eindigen
Button(
    root,
    text="Quit Steam Dashboard",
    font=FONT_MAIN,
    background="red",
    foreground=FONT_COLOR,
    command=root.destroy,
).grid(column=0, row=6)

# Knop voor about(readme.md) in een apart scherm ~ start ook bij opstarten programma, vandaar  "" OR ""(self)
Button(
    root,
    text="About",
    font=FONT_MAIN,
    background="gray",
    foreground=FONT_COLOR,
    command=open_new_window_readme or open_new_window_readme,
).grid(column=3, row=6)

# knop om te sorteren
# ******************************************************************************************************************
"""# TREEVIEW ~ window, style, data, scrollbar, column-sorting-function """
# Maakt een raamwerk in de root aan voor de tabel

separator = PanedWindow(root, bd=0, bg=BACK_COLOR, sashwidth=2)
separator.grid(column=1, row=5)
# rechter onderhoekje:
_frame = Frame(root, background=BACK_COLOR, relief="ridge")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stijlen van de Tabel treeview:
style = ttk.Style()
style.theme_use("classic")
# style.configure("Treeview.Scrollbar", foreground='red', background=back_color)
style.configure("Treeview.Heading", foreground="green", background=BACK_COLOR)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Geeft aan welke data uit de dictionairy mee te nemen
treeview = ttk.Treeview(
    root,
    show="headings",
    columns=("Name", "Developer", "Platforms", "Genre"),
    style="Treeview.Heading",
)

# Voegt Kolomkoppen toe, command = sorteerfunctie(sortby)
treeview.heading("#1", text="Name", command=lambda c="#1": sort_by(treeview, c, 0))
treeview.heading("#2", text="Developer", command=lambda c="#2": sort_by(treeview, c, 0))
treeview.heading("#3", text="Platforms", command=lambda c="#3": sort_by(treeview, c, 0))
treeview.heading("#4", text="Genre", command=lambda c="#4": sort_by(treeview, c, 0))


# Plaatst data van data_import(main) in treeview tabel
# Plaatst ook tag = 'body' om later stijl toe te voegen
for row in data_import:
    treeview.insert(
        "",
        "end",
        values=(row["name"], row["developer"], row["platforms"], row["genres"]),
        tags="body",
    )
# stijlchoice body text
treeview.tag_configure("body", background=BACK_COLOR)

# Geeft aan waar de tabel in het grid moet
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sorteert columns naar klik op de headers TODO implementeer slimmere algoritmes


def sort_by(tree, col, descending):
    # grab values to sort
    header_data = [(tree.set(child, col), child) for child in tree.get_children("")]
    header_data.sort(reverse=descending)
    for ix, item in enumerate(header_data):
        tree.move(item[1], "", ix)
    # switch the heading, so it will sort in the opposite direction.
    tree.heading(
        col, command=lambda local_col=col: sort_by(tree, local_col, int(not descending))
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SCROLLBAR van tabel
ysb = ttk.Scrollbar(orient=VERTICAL, command=treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command=treeview.xview)
treeview["yscroll"] = ysb.set
treeview["xscroll"] = xsb.set
separator.add(_frame)

# plaatst de scrollbar
ysb.grid(in_=_frame, row=0, column=1, sticky=NS)
xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
_frame.rowconfigure(0, weight=1)
_frame.columnconfigure(0, weight=1)
# attempt to color scrollbar

style.configure(
    "Vertical.TScrollbar",
    background="black",
    bordercolor="black",
    troughcolor="black",
    highlightcolor="white",
)
style.configure(
    "Horizontal.TScrollbar",
    background="black",
    bordercolor="black",
    troughcolor="black",
    highlightcolor="white",
)

# ******************************************************************************************************************
"""# FIRE ~setup, pickup data, programme, placing"""
# setup
FIRE_LABEL = Label(root, text="a", font="TkFixedFont", bg="black", fg="gold")


def get_txt1():
    fire1 = glob.glob("fire1.txt")
    text1 = open(fire1[0], "r", encoding="utf-8").read()
    return text1


def get_txt2():
    fire2 = glob.glob("fire2.txt")
    text2 = open(fire2[0], "r", encoding="utf-8").read()
    return text2


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIRE programma zelf


def moving_ascii():  # <--- Flame one direction.
    FIRE_LABEL.configure(text=get_txt1())
    FIRE_LABEL.after(FLAME_SPEED, moving_ascii2)


def moving_ascii2():  # <--- Flame other direction.
    FIRE_LABEL.configure(text=get_txt2())
    FIRE_LABEL.after(FLAME_SPEED, moving_ascii)


#


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLaatsting FIRE
FIRE_LABEL.grid(column=1, row=7)
FIRE_LABEL.after(1, moving_ascii)
# ******************************************************************************************************************
"""# Running main GUI"""
root.mainloop()
# ******************************************************************************************************************
