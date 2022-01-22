"""GUI of the Application"""
import os
import glob
import json
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

my_style_class = Style_Class(
    "black",
    "white",
    ("FF Din OT", 24, "bold"),
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
class FrameSize:
    def __init__(self,width,height,count):
        self.width = width
        self.height = height
        self.count = count


center_frame_class = FrameSize(1200, 600, 0)

class MainScreen:
    def command(self):
        root.destroy()

    def button1game(self):
        print("clicked a button, well done")
        self.configurable_label.config(
            text=list_first_game()
        )
        print(list_first_game())
        scroll_to(0)

    def button2(self):
        self.configurable_label.config(
            text=average_game_price(),
        )  # <--- TODO: this command doesnt change when table changes
        print("clicked a button, well done")

    def button3(self):
        print("clicked a button, well done")
        self.configurable_label.config(
            text=list_first_game_developers()
        )  # <--- TODO: this command doesnt change when table changes

    def button4(self):  # <--- button for searching
        print("clicked a button4, well done")
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

    def __init__(self, parent):
        self.centeringframe = Frame(parent)
        self.centeringframe["width"] = center_frame_class.width
        self.centeringframe["height"] = center_frame_class.height
        self.centeringframe["background"] = 'gray'#my_style_class.back_color
        self.centeringframe.place(relx=0.5, rely=0.5, anchor=CENTER)




        # self.button1 = Button(self.centeringframe)
        # self.button1["text"]= "Hello, World!"
        # self.button1["background"] = my_style_class.back_color
        # self.button1["foreground"] = my_style_class.font_color
        # self.button1["command"] = self.command
        # self.button1.grid(row=0, column=0, pady=10, padx=5)

        self.frame_lefttop = Frame(self.centeringframe)
        self.frame_lefttop['bg']=my_style_class.back_color,
        self.frame_lefttop['width']=center_frame_class.width,
        self.frame_lefttop['bg']=my_style_class.back_color,

        #     width=800,
        #     height=600,
        #     relief=GROOVE,
        #     borderwidth=7,
        # )
        self.frame_lefttop.grid(row=1, column=0, pady=15, padx=(15,0),sticky=W)

        # self.button1 = Button(self.centeringframe, background = my_style_class.back_color)
        # self.button1["text"]= "Hello, World!"
        # # self.button1["background"] = my_style_class.back_color
        # self.button1["foreground"] = my_style_class.font_color
        # self.button1["width"] = 50
        # self.button1["command"] = self.command
        # self.button1.grid(row=2, column=0, pady=10, padx=5, sticky=W)

        self.labeltitle = Label(
            parent,
            text="Steam APP Fantastic Five",
            font=my_style_class.font_title,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            anchor=N,
            justify=CENTER,
        )
        self.labeltitle.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.sel_title_label = Label(
        self.frame_lefttop,
        text="Selected name: ",
        font=my_style_class.font_main,
        background="green",
        fg=my_style_class.font_color,
        )
        self.sel_title_label.grid(column=0, row=3, padx=20, sticky=W)

        self.sel_item_label = Label(
            self.frame_lefttop,
            text="click on a game for a title",
            font=my_style_class.font_main,
            background=my_style_class.back_color,
            fg=my_style_class.font_color,
            width=33,
            anchor=E#  <--- without this it does NOT recentre in label after running
        )
        self.sel_item_label.grid(column=1, row=3, padx=20, sticky=E)

        self.sel_pos_label = Label(
            self.frame_lefttop,
            text="Selection positive Ratings: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_pos_label.grid(column=0, row=4, padx=20, sticky=W)

        self.selectPosRat_label = Label(
            self.frame_lefttop,
            text="click on a game for positive ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectPosRat_label.grid(column=1, row=4, columnspan=2, padx=20, sticky=E)

        self.sel_neg_label = Label(
            self.frame_lefttop,
            text="Selection Negative Ratings: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_neg_label.grid(column=0, row=5, padx=20, sticky=W)

        self.selectNegRat_label = Label(
            self.frame_lefttop,
            text="select game for negative ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectNegRat_label.grid(column=1, row=5, columnspan=2, padx=20, sticky=E)

        self.gamescore_label = Label(
            self.frame_lefttop,
            text="Selection game score",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.gamescore_label.grid(column=0, row=6, padx=20, sticky=W)

        self.selectgamescore_label = Label(
            self.frame_lefttop,
            text="0/100",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectgamescore_label.grid(column=1, row=6, columnspan=2, padx=20, sticky=E)
        # Label van eerste spel in lijst:

        self.configurable_label = Label(
            self.frame_lefttop,
            # TODO uncomment:
            text= "<<<click buttons on the left>>>",
            font=my_style_class.font_main,
            background=my_style_class.font_color,
            foreground=my_style_class.back_color,
        )
        self.configurable_label.grid(row=0, column=1, pady=20, padx=50, sticky="E")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # buttonframe for in lefttop frame
        self.button_frame = Frame(master=self.frame_lefttop, bg="purple", relief=GROOVE, borderwidth=7,
            width=200,
            height=100,
        )
        self.button_frame.grid(row=0, column=0, pady=50, padx=50, sticky=W)

        self.button = Button(
            master=self.button_frame,
            text="first_game_in_json",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button1game,
            font=("roboto", 10),
            width=30,
            cursor="target",
        )
        self.button.pack()

        self.button2 = Button(
            master=self.button_frame,
            text="average_game_price",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button2,
            font=("roboto", 10),
            width=30,
            cursor="exchange",
        )
        self.button2.pack()

        self.button3 = Button(
            master=self.button_frame,
            text="list_first_game_developer",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button3,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button3.pack()

        self.txt = Entry(
            master=self.button_frame,
            bg=my_style_class.font_color,
            fg=my_style_class.back_color,
            font=("roboto", 10),
            cursor="pencil",
            width=30,
        )

        self.txt.insert(END, """Enter here...""")
        self.txt.pack(padx=20, pady=20)

        self.button4 = Button(
            master=self.button_frame,
            text="search",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button4,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button4.pack()  #<--- TODO: SEARCH BUTTON
        # *************************************************************************************************

        self.button_quit = Button(
            self.centeringframe,
            text="Quit Steam Dashboard",
            font=my_style_class.font_main,
            background="red",
            foreground="white",
            cursor="pirate",
            command=root.destroy,
        )
        self.button_quit.grid(column=1, row=7, sticky=E, padx=20)

        # Button to open readme, also calls itself at start of programme after splash
        self.button_about = Button(
            self.centeringframe,
            text="About",
            font=my_style_class.font_main,
            background="gray",
            cursor="heart",
            fg=my_style_class.font_color,
            command=open_new_window_readme()
            or open_new_window_readme,  # <--- change to open_new_window_readme() to auto start upon launch
        )
        self.button_about.grid(column=0, row=7, sticky=W, pady=10, padx=20)

        def selItemLabelChange():
            frame_lefttop.sel_item_label['text'] = (total_info[0])

        # *************************************************************************************************
        self.FIRE_LABEL = Label(
            root,
            text="loading ASCII",
            font=("TkFixedFont"),
            bg=my_style_class.back_color,
            fg="green",
        )
        # self.FIRE_LABEL2 = Label(
        #     root,
        #     text="loading ASCII",
        #     font=("TkFixedFont"),
        #     bg=my_style_class.back_color,
        #     fg="green",
        # )
        self.FIRE_LABEL3 = Label(
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
            self.FIRE_LABEL.configure(text=get_txt1())
            self.FIRE_LABEL3.configure(text=get_txt1())

            self.FIRE_LABEL.after(my_style_class.flame_speed, moving_ascii2)

        def moving_ascii2():  # <--- Flame other direction.
            self.FIRE_LABEL.configure(text=get_txt2())
            self.FIRE_LABEL3.configure(text=get_txt2())

            self.FIRE_LABEL.after(my_style_class.flame_speed, moving_ascii)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # PLaatsting FIRE
        self.FIRE_LABEL.place(relx=0.25, rely=1, anchor=S)
        self.FIRE_LABEL3.place(relx=0.75, rely=1, anchor=S)
        self.FIRE_LABEL.after(1, moving_ascii)
        self.FIRE_LABEL3.after(1, moving_ascii)



# # *************************************************************************************************
# # raspberry setup GPIO
# #
# # # TODO: uncomment after installing on pi with package:
# # GPIO.setmode(GPIO.BCM)        # Alles hierin nodig voor Servo
# #GPIO.setup(18, GPIO.OUT)    # Servo op ping 18
# #
# # pwm=GPIO.PWM(18, 50)            # zit op pin 18, 50 hz
# # pwm.start(1)
#
# # raspberry PI function to control servo


def ratings_calc(neg_reviews, pos_reviews):
    total_reviews = neg_reviews + pos_reviews
    percentage = round((pos_reviews / total_reviews) * 100, 2)
    mainscreen.selectgamescore_label.config(text=percentage, bg="green")
    gradenaanwijziging(percentage)
    return percentage


def gradenaanwijziging(
    percentage,
):  # Functie om de Servo te laten draaien naar likes percentage
    graden = percentage / 10 + 2
    print('error: ~~~~ goto line 430ish gradenaanwijzing() and uncomment')
    # pwm.ChangeDutyCycle(2)
    # sleep(0.1)
    # pwm.ChangeDutyCycle(graden)
    print(f"moving servo to {graden} degrees at percentage {percentage}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def open_new_window_readme():
    new_window = Tk()  # <---     open new window
    new_window.overrideredirect(True)  # <--- Removes Title bar

    # set the dimensions of the screen based upon earlier code
    # and where it is placed
    new_window.geometry("860x875")


    # Achtergrond kleur van de readme (inclusief transparency)
    new_window["bg"] = my_style_class.back_color
    new_window.wait_visibility(new_window)
    new_window.wm_attributes("-alpha", 0.99)

    # De data van de README.MD
    text = Text(
        new_window,
        width=120,
        height=53,
        font="TkFixedFont",
        fg=my_style_class.font_color,
        bg=my_style_class.back_color,
    )
    text.pack()  # <--- placement of .grid seperate or scrollbar doesnt compute
    text.insert(END, get_readme())

    # # Scrollbar
    # scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=text.yview)
    # # scrollbar.pack(fill="y",side=RIGHT, expand=TRUE)
    # # Readme scrollbar style
    # my_style = ttk.Style()
    # my_style.theme_use("classic")
    # my_style.configure(
    #     "Scrollbar",
    #     background="black",
    #     bordercolor="black",
    #     arrowcolor="black",)

    # close readme
    Button(new_window, text="close", bg="red", command=new_window.destroy, width=100).pack(padx=25, pady=10
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
    root.mainloop()


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    1000,
    splashscreen.destroy,  # TODO <--- 12000ms set to 0 this one to skip splashscreen
)
# function should be "delayedstart":
splashscreen.after(2000, delayed_start)
splashscreen.after(0, print("starting splashscreen"))

splashscreen.eval("tk::PlaceWindow . center")  # <--- center splashscreen

splashscreen.mainloop()
# *************************************************************************************************
# TREEVIEW
root = Tk()
# window format:
root.eval("tk::PlaceWindow . center")  # <--- window to center screen
root.wait_visibility(root)  # <---waits, then makes page translucent
#TODO make valid
root.wm_attributes("-alpha", my_style_class.window_transparency, "-fullscreen", True)  # <---waits, then makes page translucent and fullscreen
root.configure(background=my_style_class.back_color)
mainscreen = MainScreen(root)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""# TREEVIEW ~ window, style, data, scrollbar, column-sorting-function """
# Maakt een raamwerk in de root aan voor de tabel
separator = PanedWindow(
    mainscreen.centeringframe,
    bd=0,
    bg=my_style_class.back_color,
    sashwidth=2,
    height=400,
    width=400,
)
separator.grid(row=1, column=1, pady=15, padx=(15))
# rechter onderhoekje:
_frame = Frame(
    root, background=treeview_style_class.back_color, relief="ridge"
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
# Laadt het .json bestand in een list
DATABASE_STEAM = "steam.json"
f = open(DATABASE_STEAM)
data_tree = json.load(f)
data_import = []
for line in data_tree:
    data_import.append(line)

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
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
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
    # rowID = treeview.identify('item', event.x, event.y)
    # print(rowID)
    # print(f'indetify row: {rowID}')  #<---TODO: implement Returns the item ID of the item at position y.

    treeview.rowconfigure(treeview.index(curItem), minsize=15)

    # show selected info in buttons:
    total_info = info_string.get("values")
    positive_ratings = total_info[4]  # <--- assign
    negative_ratings = total_info[5]  # <--- assign

    print(f"sel onscr. in table : total_info = {total_info}")

    mainscreen.sel_item_label.config(text=total_info[0], anchor=E)
    print(f"title = {total_info[0]}")

    print(f"positive ratings = {positive_ratings}")
    mainscreen.selectPosRat_label.config(text=positive_ratings)

    print(f"negative ratings = {negative_ratings}")

    mainscreen.selectNegRat_label.config(text=negative_ratings)
    symbol = "%"
    ratingsperc = f"{ratings_calc(total_info[5], total_info[4])}{symbol}"
    mainscreen.configurable_label.config(text=ratingsperc)  # <--- percentagecalc in action
    ratings_calc(negative_ratings, negative_ratings)


treeview.bind("<ButtonRelease-1>", cur_treeview)  # <--- grab data from clicked row


# *************************************************************************************************

# *************************************************************************************************

""" Run main GUI"""



# TODO: RASPBERRY PI get a working gpio rpio package
# pwm.stop()      # Moet aan einde van code. Of hier, of voor de root.mainloop()
# GPIO.cleanup()

root.mainloop()
