"""GUI of the Application"""
import os
from main import *
from tkinter import *
from time import sleep
import random as random
from tkinter import ttk
from steamFunctions import *
from PIL import Image, ImageTk


# TODO: RASPBERRY PI  get a working gpio rpio package > then uncomment:
# import RPi.GPIO as GPIO     # nodig voor Servo


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
        flame_speed,
    ):
        self.back_color = back_color
        self.font_color = font_color
        self.font_title = font_title
        self.font_main = font_main
        self.window_transparency = window_transparency
        self.window_size = window_size  # <--- auto adjusting frame size to needs
        self.flame_speed = flame_speed
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
    256,  # <--- flame speed
)


treeview_style_class = Style_Class(
    "black",
    "green",
    ("FF Din OT", 14, "bold"),
    (
        "Arial" or "Helvetica",
        12,
    ),
    "",  # <--- transparency locally adjusted
    "",  # <--- frame size locally adjusted
    256,  # <--- flame speed
)


# *************************************************************************************************
# TODO: RASPBERRY PI change changeable text at bottom to commits, last minute change
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
with open(splashpath, encoding="utf-8") as splash_loader_filelist:
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
        sleep(random.uniform(1, 2.2))


def delayed_start():
    change_label()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# raspberry setup GPIO
#
# # TODO: uncomment after installing on pi with package:
# GPIO.setmode(GPIO.BCM)        # Alles hierin nodig voor Servo
# GPIO.setup(18, GPIO.OUT)    # Servo op ping 18
#
# pwm=GPIO.PWM(18, 50)            # zit op pin 18, 50 hz
# pwm.start(1)

# raspberry PI function to control servo


def ratings_calc(neg_reviews, pos_reviews):
    total_reviews = neg_reviews + pos_reviews
    percentage = round((pos_reviews / total_reviews) * 100, 2)
    selectgamescore_label.config(text=percentage, bg="green")
    gradenaanwijziging(percentage)
    return percentage


def gradenaanwijziging(
    percentage,
):  # Functie om de Servo te laten draaien naar likes percentage
    graden = percentage / 10 + 2
    pwm.ChangeDutyCycle(2)
    sleep(0.1)
    pwm.ChangeDutyCycle(graden)
    print(f"moving servo to {graden} degrees at percentage {percentage}")


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
_frame = Frame(
    centering_frame, background=treeview_style_class.back_color, relief="ridge"
)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stijlen van de Tabel treeview:
style = ttk.Style()
style.theme_use("classic")
style.configure(
    "Treeview.Heading",
    rowheight=21,
    foreground=treeview_style_class.font_color,
    background=treeview_style_class.back_color,
)  # <--- creates the basic table style

style.map(
    "Treeview.Heading",
    background=[("selected", treeview_style_class.font_color)],
    foreground=[("selected", treeview_style_class.back_color)],
)  # <--- this function changes style selected row
# TODO: change column top colour


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
)  # <--- this sets up the columns

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
""""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/treeview.html

Setting a custom sort function
It is also possible to set a custom comparison function in order to change the sorting behaviour. As an example we will create a comparison function that sorts case-sensitive. In the example above the sorted list looked like:

alfred
Alfred
benjamin
Benjamin
charles
Charles
david
David
The case-sensitive sorted list will look like:

Alfred
Benjamin
Charles
David
alfred
benjamin
charles
david
First of all a comparison function is needed. This function gets two rows and has to return a negative integer if the first one should come before the second one, zero if they are equal and a positive integer if the second one should come before the first one.

def compare(model, row1, row2, user_data):
    sort_column, _ = model.get_sort_column_id()
    value1 = model.get_value(row1, sort_column)
    value2 = model.get_value(row2, sort_column)
    if value1 < value2:
        return -1
    elif value1 == value2:
        return 0
    else:
        return 1
Then the sort function has to be set by Gtk.TreeSortable.set_sort_func().

model.set_sort_func(0, compare, None)"""


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
    highlightcolor="purple",
)

# TODO implement this into a search function, add select row
def scroll_to(line):
    # line=index(average_game_price())

    treeview.yview_moveto(0)  # <--- resets scroll to top
    sleep(0.001)
    treeview.yview_scroll(line - 1, "unit")
    child_id = treeview.get_children()[
        line
    ]  # <--- picks up on the id of the row in row 1=2
    print(f"child_id = {child_id}")
    curItem = treeview.focus(
        child_id
    )  # <--- sets curItem as the selected row of child_id
    treeview.selection_set(curItem)  # <--- colors and sets selection in treeview


# *************************************************************************************************
# Grab info selected row treeview

# this block is needed to keep the column sorter running properly in conjunction with cur_treeview:
child_id = treeview.get_children()[100]  # <--- picks up on the id of the row in row 1=2
print(f"child_id = {child_id}")
curItem = treeview.focus(child_id)  # <--- sets curItem as the selected row of child_id
treeview.selection_set(child_id)  # <--- colors and sets selection in treeview


def cur_treeview(a):

    curItem = treeview.focus()
    info_string = treeview.item(curItem)
    print(f"info_string = treeview.item(curItem) = {info_string}")
    print(curItem)
    print(treeview.index(curItem))

    treeview.rowconfigure(treeview.index(curItem), minsize=15)

    # show selected info in buttons:
    total_info = info_string.get("values")
    positive_ratings = total_info[4]  # <--- assign
    negative_ratings = total_info[5]  # <--- assign

    print(f"sel onscr. in table : total_info = {total_info}")
    sel_item_label.config(text=total_info[0], anchor=E)
    print(f"title = {total_info[0]}")

    print(f"positive ratings = {positive_ratings}")
    selectPosRat_label.config(text=positive_ratings)

    print(f"negative ratings = {negative_ratings}")

    selectNegRat_label.config(text=negative_ratings)
    symbol = "%"
    ratingsperc = f"{ratings_calc(total_info[5], total_info[4])}{symbol}"
    configurable_label.config(text=ratingsperc)  # <--- percentagecalc in action
    ratings_calc(negative_ratings, negative_ratings)


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
    text="Selection game score",
    font=my_style_class.font_main,
    background="green",
    fg=my_style_class.font_color,
)
gamescore_label.grid(column=0, row=6, padx=20, sticky=W)

selectgamescore_label = Label(
    frame_lefttop,
    text="0/100",
    font=my_style_class.font_main,
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
)
selectgamescore_label.grid(column=1, row=6, columnspan=2, padx=20, sticky=E)
# Label van eerste spel in lijst:

configurable_label = Label(
    frame_lefttop,
    text=first_game_in_json,
    font=my_style_class.font_main,
    background=my_style_class.font_color,
    foreground=my_style_class.back_color,
)
configurable_label.grid(row=0, column=1, pady=20, padx=50, sticky="E")


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
    )
    print(list_first_game_developers())
    scroll_to(1)


def button2():
    configurable_label.config(
        text=average_game_price(),
    )  # <--- TODO: this command doesnt change when table changes
    print("clicked a button, well done")


def button3():
    print("clicked a button, well done")
    configurable_label.config(
        text=first_game_in_json,
    )  # <--- TODO: this command doesnt change when table changes


def button4():  # <--- button for searching
    print("clicked a button, well done")
    # Importeer json om steam.json correct uit te lezen.
    # import json

    # Het json bestand uitlezen en opslaan als variable.
    source = open("steam_small.json", encoding="utf-8")
    data = json.load(source)

    # Lees de titles uit bestand, en voor de eerste die dezelfde als input is, slaat regel op
    for line in data:
        index = +1  # <--- counts lines
        if line.get("name") == "Counter-Strike":
            print(index)
            scroll_to(index)
            return index  # TODO add scrolltocursor
    # <--- TODO: this command doesnt change when table changes


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
    cursor="target",
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
    cursor="exchange",
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
    cursor="man",
)
button3.pack()

txt = Entry(
    master=frame,
    bg=my_style_class.font_color,
    fg=my_style_class.back_color,
    font=("roboto", 10),
    cursor="pencil",
    width=30,
)

txt.insert(END, """Enter here...""")
txt.pack(padx=20, pady=20)

button4 = Button(
    master=frame,
    text="search",
    bg=my_style_class.back_color,
    fg=my_style_class.font_color,
    command=button4,
    font=("roboto", 10),
    width=30,
    cursor="man",
)
button4.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Buttons in the mainscreen
# Button to terminate mainscreen
Button(
    centering_frame,
    text="Quit Steam Dashboard",
    font=my_style_class.font_main,
    background="red",
    foreground="white",
    cursor="pirate",
    command=root.destroy,
).grid(column=1, row=7, sticky=E, padx=20)

# Button to open readme, also calls itself at start of programme after splash
Button(
    centering_frame,
    text="About",
    font=my_style_class.font_main,
    background="gray",
    cursor="heart",
    fg=my_style_class.font_color,
    # TODO: before final presentation, uncomment this section DO NOT DELETE
    # command=open_new_window_readme()
    # or open_new_window_readme,  # <--- change to open_new_window_readme() to auto start upon launch
).grid(column=0, row=7, sticky=W, pady=10, padx=20)

# *************************************************************************************************


"""# FIRE ~setup, pickup data, programme, placing"""
# setup

FIRE_LABEL = Label(
    root,
    text="loading ASCII",
    font=("TkFixedFont"),
    bg=my_style_class.back_color,
    fg="green",
)
FIRE_LABEL2 = Label(
    root,
    text="loading ASCII",
    font=("TkFixedFont"),
    bg=my_style_class.back_color,
    fg="green",
)
FIRE_LABEL3 = Label(
    root,
    text="loading ASCII",
    font=("TkFixedFont"),
    bg=my_style_class.back_color,
    fg="green",
)
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

    FIRE_LABEL.after(my_style_class.flame_speed, moving_ascii2)


def moving_ascii2():  # <--- Flame other direction.
    FIRE_LABEL.configure(text=get_txt2())
    FIRE_LABEL3.configure(text=get_txt2())

    FIRE_LABEL.after(my_style_class.flame_speed, moving_ascii)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLaatsting FIRE
FIRE_LABEL.place(relx=0.25, rely=1, anchor=S)
FIRE_LABEL3.place(relx=0.75, rely=1, anchor=S)
FIRE_LABEL.after(1, moving_ascii)
FIRE_LABEL3.after(1, moving_ascii)


# *************************************************************************************************

""" Run main GUI"""
root.eval("tk::PlaceWindow . center")  # <--- center screen
# TODO: RASPBERRY PI get a working gpio rpio package
# pwm.stop()      # Moet aan einde van code. Of hier, of voor de root.mainloop()
# GPIO.cleanup()
root.mainloop()
# *************************************************************************************************
