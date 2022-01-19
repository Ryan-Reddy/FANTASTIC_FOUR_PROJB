"""GUI of the Application"""
import os
import random
import time
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from main import *
from steamFunctions import *

# *************************************************************************************************
"""STYLE/COLOR CHOICES

Tkinter kleurkeuzes ***Alleen deze wijzigen!***:
"""


class Style_Class:
    def __init__(
        self,
        back_color,
        font_color,
        font_title,
        font_main,
        window_transparency,
        window_size,
    ):
        self.back_color = back_color
        self.font_color = font_color
        self.font_title = font_title
        self.font_main = font_main
        self.window_transparency = window_transparency
        self.window_size = window_size  # <--- auto adjusting frame size to needs
        # self.pack = pack


my_style_class = Style_Class(
    "black",
    "white",
    ("FF Din OT", 14, "bold"),
    (
        "Arial" or "Helvetica",
        12,
    ),
    0.9,
    "",  # <--- auto adjusting frame size to needs
)

treeview_style_class = Style_Class(
    "black",
    "white",
    ("FF Din OT", 14, "bold"),
    (
        "Arial" or "Helvetica",
        12,
    ),
    "",  # <--- transparency locally adjusted
    "",  # <--- frame size locally adjusted
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TODO: edit following styles out.


FLAME_SPEED = 256


# *************************************************************************************************
# TODO: change changeable text at bottom to commits, last minute change
"""# SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme"""

splashscreen = Tk()  # <--- setup splashscreen
splashscreen.overrideredirect(True)  # <--- Removes TITELBALK

splashscreen.call("wm", "attributes", ".", "-topmost", "true")  # <--- # topmost screen

splashscreen.geometry(
    "960x307"
)  # <--- # size of screen + positie (steam-logo-large.jpg = 960x307)
splashscreen.geometry(
    my_style_class.window_size
)  # <--- autoadjust overrides upper geometry
# Achtergrond kleur van de readme (inclusief transparency)
splashscreen["bg"] = my_style_class.back_color
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# input splashscreen picture order file:
splashpath = os.path.join("splashscreen", "splash.txt")
with open(splashpath) as splash_loader_filelist:
    splash_order = splash_loader_filelist.read().splitlines()
    splash_loader_filelist.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #  Calculates center of active screen
# w = 980  # width for the readme root
# h = 680  # height for the readme root
#
#
# # get screen width and height
# SPLASH_WIDTH = splashscreen.winfo_screenwidth()  # width of the screen
# SPLASH_HEIGHT = splashscreen.winfo_screenheight()  # height of the screen
#
# # calculate x and y coordinates for the Tk root window
# WINDOW_xMIDDLE = (SPLASH_WIDTH / 2) - (w / 2)
# WINDOW_yMIDDLE = (SPLASH_HEIGHT / 2) - (h / 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# initial fill splashscreen
img = Image.open(splash_order[0])
ph = ImageTk.PhotoImage(img)
img_label = Label(splashscreen, image=ph)
img_label.pack()
splash_label = Label(
    splashscreen, text="loading", bg=my_style_class.back_color, fg="gold"
)
splash_label.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen programme:
splashscreen.after(
    0,
    splashscreen.destroy,  # TODO <--- 12000ms set to 0 this one to skip splashscreen
)
# function should be "delayedstart":
splashscreen.after(2000, delayed_start)
splashscreen.after(0, print("starting splashscreen"))

splashscreen.eval("tk::PlaceWindow . center")  # <--- center splashscreen

splashscreen.mainloop()
# *************************************************************************************************

""" README SCREEN GUI:"""


def open_new_window_readme():
    new_window = Tk()  # <---     open new window
    # new_window.overrideredirect(True)  # <--- Removes Title bar

    # set the dimensions of the screen based upon earlier code
    # and where it is placed
    new_window.geometry("700x600")

    # new_window.title("READ ME PLEASE")  # <---     sets the title readme
    new_window.call(
        "wm", "attributes", ".", "-topmost", "true"
    )  # <--- # topmost screen

    # Achtergrond kleur van de readme (inclusief transparency)
    new_window["bg"] = my_style_class.back_color
    new_window.wait_visibility(new_window)
    new_window.wm_attributes("-alpha", 1)

    # De data van de README.MD
    text = Text(
        new_window,
        width=120,
        height=40,
        font="TkFixedFont",
        fg=my_style_class.font_color,
        bg=my_style_class.back_color,
    )
    text.grid(row=0)  # <--- placement of .grid seperate or scrollbar doesnt compute
    text.insert(END, get_readme())

    # Scrollbar
    scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=text.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    # Readme scrollbar style
    my_style = ttk.Style()
    # my_style.theme_use("classic")
    my_style.configure(
        "Scrollbar",
        background="black",
        bordercolor="black",
        arrowcolor="black",
    )

    # close readme
    Button(new_window, text="close", bg="red", command=new_window.destroy).grid(
        row=1, sticky=W + E, padx=20, pady=10
    )


# *************************************************************************************************
"""# MAIN-SCREEN ~ GUI settings:"""
root = Tk()
# Raam formaat:
root.geometry(my_style_class.window_size)

root.eval("tk::PlaceWindow . center")  # <--- window to center screen

# Achtergrond kleur:
root["bg"] = my_style_class.back_color
root.wait_visibility(root)  # <---waits, then makes page translucent
root.wm_attributes("-alpha", my_style_class.window_transparency, "-fullscreen", True)


# window_name.attributes('-fullscreen',True)

# *************************************************************************************************

"""# MAIN SCREEN ~ Labels and Buttons:"""
# TODO build a frame to rule them all, and then center on screen
centering_frame = Frame(
    root,
    bg=my_style_class.back_color,
    width=600,
    height=600,
    relief=GROOVE,
    borderwidth=7,
)
centering_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

# lefttop frame (frame in root)
frame_lefttop = Frame(
    centering_frame,
    bg=my_style_class.back_color,
    width=800,
    height=600,
    relief=GROOVE,
    borderwidth=7,
)
frame_lefttop.grid(row=1, column=0, pady=10, padx=5)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""# TREEVIEW ~ window, style, data, scrollbar, column-sorting-function """
# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(
    centering_frame,
    bd=0,
    bg=my_style_class.back_color,
    sashwidth=2,
    height=320,
    width=400,
)
separator.grid(row=1, column=1)
# rechter onderhoekje:
_frame = Frame(centering_frame, background=my_style_class.back_color, relief="ridge")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stijlen van de Tabel treeview:
style = ttk.Style()
style.theme_use("classic")
style.configure(
    "Treeview.Heading", foreground=treeview_style_class.font_color,background=treeview_style_class.back_color

)
style.map('Treeview.Heading', background=[('selected', '#BFBFBF')], foreground=[('selected', 'black')])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
treeview.tag_configure("body", background=my_style_class.back_color)

# Geeft aan waar de tabel in het grid moet
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW, pady=10, padx=(5, 0))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sorteert columns naar klik op de headers TODO implementeer slimmere algoritmes


def sort_by(tree, col, descending):
    # grab values to sort
    header_data = [(tree.set(child, col), child) for child in tree.get_children("")]
    header_data.sort(reverse=descending)
    # TODO if the data to be sorted is numeric change to float
    # data =  change_numeric(data)

    # now sort the data in placej
    for ix, item in enumerate(header_data):
        tree.move(item[1], "", ix)
    # switch the heading, so it will sort in the opposite direction.
    tree.heading(
        col, command=lambda local_col=col: sort_by(tree, local_col, int(not descending))
    )


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SCROLLBAR van tabel
ysb = ttk.Scrollbar(orient=VERTICAL, command=treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command=treeview.xview)
treeview["yscroll"] = ysb.set
treeview["xscroll"] = xsb.set
separator.add(_frame)

# plaatst de scrollbar
ysb.grid(in_=_frame, row=0, column=1, sticky=NS, pady=10, padx=(0, 10))
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

# *************************************************************************************************
# Grab info selected row treeview
#
# def gamescore_calculator():
#     if total_info[5] > total_info[4]:
#         score = total_info[5] / total_info[4]*5
#         return score
#     if total_info[4] > total_info[5]:
#         score = (total_info[4] / total_info[5]*5)+5
#         return score


def cur_treeview(a):
    curItem = treeview.focus()
    info_string = treeview.item(curItem)
    print(f'info_string = treeview.item(curItem) = {info_string}')
    print(curItem)
    print(treeview.index(curItem))

    treeview.rowconfigure(treeview.index(curItem), minsize=15)

    #
    # style.configure(
    #     "curItem",
    #     background="gray",
    #     bordercolor="black",
    #     troughcolor="black",
    #     highlightcolor="white",
    # )


    total_info = info_string.get("values")
    print(f"sel onscr. in table : total_info = {total_info}")
    sel_item_label.config(text=total_info[0])
    print(f"title = {total_info[0]}")

    selectNegRat_label.config(text=total_info[5])
    print(f"positive ratings = {total_info[4]}")

    selectPosRat_label.config(text=total_info[4])
    print(f"negative ratings = {total_info[5]}")

    if total_info[5] > total_info[4]:  #<--- neg > pos
        print(total_info[4] / total_info[5])
        score = ((total_info[4] / total_info[5])*5)  #<--- creates a factor, then scales to 5 for more neg than pos it keeps it under 5
        selectgamescore_label.config(text=score, bg='red')

    if total_info[4] > total_info[5]:  #<--- pos > neg
        print(total_info[5] / total_info[4])
        score = ((total_info[5] / total_info[4])*5)+5  #<--- creates a factor, then scales to 5 for more pos than neg it keeps it over 5
        selectgamescore_label.config(text=score, bg='green')


treeview.bind("<ButtonRelease-1>", cur_treeview)  # <--- grab data from clicked row


# *************************************************************************************************


# De labels die je ziet op scherm
# TITEL
Label(
    root,
    text="Steam APP Fantastic Five",
    font=my_style_class.font_title,
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
    anchor=N,
    justify=CENTER,
).place(relx=0.5, rely=0.1, anchor=CENTER)


# lefttop frame contents

# Labels

#  clickbuttonlabels
sel_title_label = Label(
    frame_lefttop,
    text="Selected name: ",
    font=my_style_class.font_main,
    background="green",
    fg=my_style_class.font_color,
)
sel_title_label.grid(column=0, row=3, padx=20, sticky=W)

sel_item_label = Label(
    frame_lefttop,
    text="" "",
    font=my_style_class.font_main,
    background=my_style_class.back_color,
    fg=my_style_class.font_color,
    width=50,  # <--- without this it does NOT recentre in label after running
)
sel_item_label.grid(column=1, row=3, padx=20, sticky=E)


sel_pos_label = Label(
    frame_lefttop,
    text="Selection positive Ratings: ",
    font=my_style_class.font_main,
    background="green",
    fg=my_style_class.font_color,
)
sel_pos_label.grid(column=0, row=4, padx=20, sticky=W)


selectPosRat_label = Label(
    frame_lefttop,
    text="click on a game for positive ratings",
    font=my_style_class.font_main,
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
)
selectPosRat_label.grid(column=1, row=4, columnspan=2, padx=20, sticky=E)

sel_neg_label = Label(
    frame_lefttop,
    text="Selection Negative Ratings: ",
    font=my_style_class.font_main,
    background="green",
    fg=my_style_class.font_color,
)
sel_neg_label.grid(column=0, row=5, padx=20, sticky=W)

selectNegRat_label = Label(
    frame_lefttop,
    text="select game for negative ratings",
    font=my_style_class.font_main,
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
)
selectNegRat_label.grid(column=1, row=5, columnspan=2, padx=20, sticky=E)

gamescore_label = Label(
    frame_lefttop,
    text="Selection game score (under 1 = negative, above 1 = positive:",
    font=my_style_class.font_main,
    background="green",
    fg=my_style_class.font_color,
)
gamescore_label.grid(column=0, row=6, padx=20, sticky=W)

selectgamescore_label = Label(
    frame_lefttop,
    text="0/10",
    font=my_style_class.font_main,
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
)
selectgamescore_label.grid(column=1, row=6, columnspan=2, padx=20, sticky=E)


# Label van eerste spel in lijst:

# Label(
#     frame_lefttop,
#     text="First game in list:",
#     font=my_style_class.font_main,
#     background=my_style_class.back_color,
#     fg=my_style_class.font_color,
# ).grid(column=0, row=2, sticky=W, padx=20)

configurable_label = Label(
    frame_lefttop,
    text=first_game_in_json,
    font=my_style_class.font_main,
    background="yellow",
    foreground="black",
)
configurable_label.grid(row=0, column=1, pady=50, padx=50, sticky="E")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   BUTTONS
# buttonframe for in lefttop frame
button_frame = Frame(
    master=frame_lefttop,
    bg=my_style_class.back_color,
    width=20,
    height=10,
    relief=GROOVE,
    borderwidth=7,
)
button_frame.grid(row=0, column=0, pady=50, padx=50, sticky=W)




# filters based upon values: ex foldout menu with all the platforms, changes the table to show only all the windows games
# one for each column


def button1():
    print("clicked a button, well done")
    configurable_label.config(
        text=list_first_game_developers()
    )  # <--- TODO: this command doesnt change when table changes


def button2():
    print("clicked a button, well done")
    configurable_label.config(
        text=average_game_price()
    )  # <--- TODO: this command doesnt change when table changes


def button3():
    print("clicked a button, well done")
    configurable_label.config(
        text=first_game_in_json,
    )  # <--- TODO: this command doesnt change when table changes


frame = Frame(master=button_frame, bg="purple", relief=GROOVE, borderwidth=7)
frame.grid(row=0, column=0, padx=5, pady=5)

button = Button(
    master=frame,
    text="first_game_in_json",
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
    command=button1,
    font=("roboto", 10),
    width=30,
)
button.pack()

button2 = Button(
    master=frame,
    text="average_game_price",
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
    command=button2,
    font=("roboto", 10),
    width=30,
)
button2.pack()

button3 = Button(
    master=frame,
    text="list_first_game_developers",
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
    command=button3,
    font=("roboto", 10),
    width=30,
)
button3.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Buttons in the mainscreen
# Button to terminate mainscreen
Button(
    centering_frame,
    text="Quit Steam Dashboard",
    font=my_style_class.font_main,
    background="red",
    foreground="white",
    command=root.destroy,
).grid(column=1, row=7, sticky=E, padx=20)

# Button to open readme, also calls itself at start of programme after splash
Button(
    centering_frame,
    text="About",
    font=my_style_class.font_main,
    background="gray",
    fg=my_style_class.font_color,
    # TODO: before final presentation, uncomment this section DO NOT DELETE
    # command=open_new_window_readme()
    # or open_new_window_readme,  # <--- change to open_new_window_readme() to auto start upon launch
).grid(column=0, row=7, sticky=W, pady=10, padx=20)

# *************************************************************************************************


"""# FIRE ~setup, pickup data, programme, placing"""
# setup

FIRE_LABEL = Label(root, text="loading ASCII", font=("TkFixedFont"), bg=my_style_class.back_color, fg="green")
FIRE_LABEL2 = Label(root, text="loading ASCII", font=("TkFixedFont"), bg=my_style_class.back_color, fg="green")
FIRE_LABEL3 = Label(root, text="loading ASCII", font=("TkFixedFont"), bg=my_style_class.back_color, fg="green")
fire1 = glob.glob("fire1.txt")
fire2 = glob.glob("fire2.txt")


def get_txt1():
    text1 = open(fire1[0], "r", encoding="utf-8").read()
    return text1


def get_txt2():
    text2 = open(fire2[0], "r", encoding="utf-8").read()
    return text2


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIRE programma zelf


def moving_ascii():  # <--- Flame one direction.
    FIRE_LABEL.configure(text=get_txt1())
    FIRE_LABEL3.configure(text=get_txt1())

    FIRE_LABEL.after(FLAME_SPEED, moving_ascii2)


def moving_ascii2():  # <--- Flame other direction.
    FIRE_LABEL.configure(text=get_txt2())
    FIRE_LABEL3.configure(text=get_txt2())

    FIRE_LABEL.after(FLAME_SPEED, moving_ascii)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLaatsting FIRE
FIRE_LABEL.place(relx=0.25, rely=1, anchor=S)
FIRE_LABEL3.place(relx=0.75, rely=1, anchor=S)
FIRE_LABEL.after(1, moving_ascii)
FIRE_LABEL3.after(1, moving_ascii)


# *************************************************************************************************

""" Run main GUI"""
root.eval("tk::PlaceWindow . center")  # <--- center screen

root.mainloop()
# *************************************************************************************************
