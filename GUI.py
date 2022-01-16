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
TRANSPARENCY_BACKGROUND = 1  # <--- transparency mainscreen
FLAME_SPEED = 256
WINDOW_SIZE = ""  # <--- Autoadjusts to content
# ******************************************************************************************************************
# TODO: change changeable text at bottom to commits, last minute change
"""# SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme"""

splashscreen = Tk()  # <--- setup splashscreen
splashscreen.overrideredirect(True)  # <--- Removes TITELBALK

splashscreen.call("wm", "attributes", ".", "-topmost", "true")  # <--- # topmost screen

splashscreen.geometry(
    "960x307"
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
#  Calculates center of active screen
w = 980  # width for the readme root
h = 680  # height for the readme root


# get screen width and height
SPLASH_WIDTH = splashscreen.winfo_screenwidth()  # width of the screen
SPLASH_HEIGHT = splashscreen.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
WINDOW_xMIDDLE = (SPLASH_WIDTH / 2) - (w / 2)
WINDOW_yMIDDLE = (SPLASH_HEIGHT / 2) - (h / 2)
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
    2000, splashscreen.destroy  # <--- 12000ms set to 0 this one to skip splashscreen
)
# function should be "delayedstart":
splashscreen.after(2000, delayed_start)
splashscreen.after(0, print("starting splashscreen"))

splashscreen.eval("tk::PlaceWindow . center")  # <--- center splashscreen

splashscreen.mainloop()
# ******************************************************************************************************************
""" README SCREEN GUI:"""


def open_new_window_readme():
    new_window = Tk()  # <---     open new window
    # new_window.overrideredirect(True)  # <--- Removes Title bar

    # set the dimensions of the screen based upon earlier code
    # and where it is placed
    new_window.geometry("")

    # new_window.title("READ ME PLEASE")  # <---     sets the title readme
    new_window.call(
        "wm", "attributes", ".", "-topmost", "true"
    )  # <--- # topmost screen

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
    my_style.theme_use("classic")
    my_style.configure(
        "Vertical.TScrollbar",
        background="black",
        bordercolor="black",
        arrowcolor="white",
    )

    # close readme
    Button(new_window, text="close", bg="red", command=new_window.destroy).grid(row=1)


# ******************************************************************************************************************
"""# MAIN-SCREEN ~ GUI settings:"""
root = Tk()
# Raam formaat:
root.geometry(WINDOW_SIZE)

root.eval("tk::PlaceWindow . center")  # <--- window to center screen

# Achtergrond kleur:
root["bg"] = BACK_COLOR
root.wait_visibility(root)  # <---waits, then makes page translucent
root.wm_attributes("-alpha", TRANSPARENCY_BACKGROUND, "-fullscreen", True)
# window_name.attributes('-fullscreen',True)

# ******************************************************************************************************************
"""# MAIN SCREEN ~ Labels and Buttons:"""

# lefttop frame (frame in root)
frame_lefttop = Frame(
    root,
    bg=BACK_COLOR,
    width=800,
    height=600,
    relief=GROOVE,
    borderwidth=7,
).grid(row=1, column=0)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# buttonframe for in lefttop frame
button_frame = Frame(
    master=root,
    bg=BACK_COLOR,
    width=800,
    height=600,
    relief=GROOVE,
    borderwidth=7,
)
button_frame.grid(row=1, column=0, pady=50, padx=50, sticky="W")
for i in range(10):
    for j in range(1):
        frame = Frame(master=button_frame, bg="gray", relief=GROOVE, borderwidth=7)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = Button(
            master=frame,
            text=f"Button {i}x{j}",
            bg=BACK_COLOR,
            fg=FONT_COLOR,
            font=("roboto", 10),
            width=30,
        )
        label.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# textlist for in lefttop frame
textlist_frame = Frame(
    master=root,
    bg=BACK_COLOR,
    # width=800,
    # height=600,
    relief=GROOVE,
    borderwidth=7,
)
textlist_frame.grid(row=1, column=0, pady=50, padx=50, sticky="E")

w = Listbox(
    master=textlist_frame,
    bg=BACK_COLOR,
    fg=FONT_COLOR,
    width=10,
    height=10,
    listvariable=splash_order,
).pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Buttons in the mainscreen
# Button to terminate mainscreen
Button(
    root,
    text="Quit Steam Dashboard",
    font=FONT_MAIN,
    background="red",
    foreground=FONT_COLOR,
    command=root.destroy,
).grid(column=1, row=5, sticky=E, padx=20)

# Button to open readme, also calls itself at start of programme after splash
Button(
    root,
    text="About",
    font=FONT_MAIN,
    background="gray",
    foreground=FONT_COLOR,
    command=open_new_window_readme()
    or open_new_window_readme,  # <--- change to open_new_window_readme() to auto start upon launch
).grid(column=0, row=5, sticky=W, padx=20)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Label van eerste spel in lijst:

Label(
    frame_lefttop,
    text="First game in list:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=2, sticky=W, padx=20)

Label(
    frame_lefttop,
    text=first_game_in_json,
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=0, row=2, sticky=E, padx=20)

# label van gemiddelde prijs van de games:
Label(
    root,
    text="Average game price:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=3, sticky=W, padx=20)
Label(
    root,
    text=average_game_price(),
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=0, row=3, sticky=E, padx=20)

# Label van eerste game dev in de lijst:
Label(
    root,
    text="First game developer:",
    font=FONT_MAIN,
    background=BACK_COLOR,
    foreground=FONT_COLOR,
).grid(column=0, row=4, sticky=W, padx=20)
Label(
    root,
    text=list_first_game_developers(),
    font=FONT_MAIN,
    background="yellow",
    foreground="black",
).grid(column=0, row=4, sticky=E, padx=20)

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
).grid(row=0, column=0, columnspan=(2))


# ******************************************************************************************************************
"""# TREEVIEW ~ window, style, data, scrollbar, column-sorting-function """
# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(root, bd=0, bg=BACK_COLOR, sashwidth=2, height=600, width=800)
separator.grid(row=1, column=1)
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
    columns=(
        "Name",
        "Developer",
        "Platforms",
        "Genre",
        "Positive Ratings",
        "Negative Ratings",
        "Required Age",
        "Publisher",
    ),
    style="Treeview.Heading",
)

# Voegt Kolomkoppen toe, command = sorteerfunctie(sortby)
treeview.heading("#1", text="Name", command=lambda c="#1": sort_by(treeview, c, 0))
treeview.heading("#2", text="Developer", command=lambda c="#2": sort_by(treeview, c, 0))
treeview.heading("#3", text="Platforms", command=lambda c="#3": sort_by(treeview, c, 0))
treeview.heading("#4", text="Genre", command=lambda c="#4": sort_by(treeview, c, 0))
treeview.heading(
    "#5", text="Positive Ratings", command=lambda c="#5": sort_by(treeview, c, 0)
)
treeview.heading(
    "#7", text="Required Age", command=lambda c="#7": sort_by(treeview, c, 0)
)
treeview.heading("#8", text="Publisher", command=lambda c="#8": sort_by(treeview, c, 0))
treeview.heading(
    "#6", text="Negative Ratings", command=lambda c="#6": sort_by(treeview, c, 0)
)


# Plaatst data van data_import(main) in treeview tabel
# Plaatst ook tag = 'body' om later stijl toe te voegen
for row in data_import:
    treeview.insert(
        "",
        "end",
        values=(
            row["name"],
            row["developer"],
            row["platforms"],
            row["genres"],
            row["positive_ratings"],
            row["negative_ratings"],
            row["required_age"],
            row["publisher"],
        ),
        tags="body",
    )
# stijlchoice body text
treeview.tag_configure("body", background=BACK_COLOR)

# Geeft aan waar de tabel in het grid moet
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sorteert columns naar klik op de headers TODO implementeer slimmere algoritmes


def sort_by(tree, col, descending):
    print("beginning at 0")
    t0 = time.perf_counter_ns()

    # grab values to sort
    header_data = [(tree.set(child, col), child) for child in tree.get_children("")]
    header_data.sort(reverse=descending)
    # TODO if the data to be sorted is numeric change to float
    # data =  change_numeric(data)

    # now sort the data in place
    for ix, item in enumerate(header_data):
        tree.move(item[1], "", ix)
    # switch the heading, so it will sort in the opposite direction.

    t1 = time.perf_counter_ns() - t0

    print("endtime = ", t1, " ms")
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
FIRE_LABEL = Label(root, text="a", font="TkFixedFont", bg="black", fg="green")
FIRE_LABEL2 = Label(root, text="a", font="TkFixedFont", bg="black", fg="green")
FIRE_LABEL3 = Label(root, text="a", font="TkFixedFont", bg="black", fg="green")


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
    FIRE_LABEL3.configure(text=get_txt1())

    FIRE_LABEL.after(FLAME_SPEED, moving_ascii2)


def moving_ascii2():  # <--- Flame other direction.
    FIRE_LABEL.configure(text=get_txt2())
    FIRE_LABEL3.configure(text=get_txt2())

    FIRE_LABEL.after(FLAME_SPEED, moving_ascii)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLaatsting FIRE
FIRE_LABEL.grid(column=0, row=8)
FIRE_LABEL3.grid(column=1, row=8)
FIRE_LABEL.after(1, moving_ascii)
FIRE_LABEL3.after(1, moving_ascii)


# ******************************************************************************************************************
""" Run main GUI"""
root.eval("tk::PlaceWindow . center")  # <--- center screen

root.mainloop()
# ******************************************************************************************************************
