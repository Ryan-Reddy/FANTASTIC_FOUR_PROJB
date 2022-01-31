"""GUI of the Application"""
import glob
from time import sleep
import random as random
from tkinter import ttk
from steamFunctions import *
from tkinter.messagebox import *
import sqlite3
from tkinter import *
import time
from PIL import Image, ImageTk
import os
from working_API_to_sql import *
from threading import Thread
import sqlite3
import json
import requests


# TODO: RASPBERRY PI  get a working gpio rpio package > then uncomment:
# import RPi.GPIO as GPIO     # nodig voor Servo


# *************************************************************************************************
"""STYLE/COLOR CHOICES
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
    0.8,
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
    def __init__(self, width, height, count):
        self.width = width
        self.height = height
        self.count = count


center_frame_class = FrameSize(1200, 600, 0)


class MainScreen:
    def destuction_imminent(self):
        shutdowncommand

    def button1game(self):
        print("clicked a button, well done")
        self.configurable_label.config(text=list_first_game())
        print(list_first_game())

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

    def __init__(self, parent):
        self.centeringframe = Frame(parent)
        self.centeringframe["width"] = center_frame_class.width
        self.centeringframe["height"] = center_frame_class.height
        self.centeringframe["background"] = "black"  # my_style_class.back_color
        self.centeringframe["relief"] = GROOVE
        self.centeringframe["borderwidth"] = 7
        self.centeringframe.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.frame_lefthalf = Frame(self.centeringframe)
        self.frame_lefthalf["bg"] = (my_style_class.back_color,)
        self.frame_lefthalf["width"] = (center_frame_class.width,)
        self.frame_lefthalf.grid(row=1, column=0, pady=15, padx=(15, 0), sticky=W)

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
            self.frame_lefthalf,
            text="Selected name: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_title_label.grid(column=0, row=3, padx=20, sticky=W)

        self.sel_item_label = Label(
            self.frame_lefthalf,
            text="click on a game for a title",
            font=my_style_class.font_main,
            background=my_style_class.back_color,
            fg=my_style_class.font_color,
            width=33,
            anchor=E,  #  <--- without this it does NOT recentre in label after running
        )
        self.sel_item_label.grid(column=1, row=3, padx=20, sticky=E)

        self.sel_pos_label = Label(
            self.frame_lefthalf,
            text="Selection positive Ratings: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_pos_label.grid(column=0, row=4, padx=20, sticky=W)

        self.selectPosRat_label = Label(
            self.frame_lefthalf,
            text="click on a game for positive ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectPosRat_label.grid(column=1, row=4, columnspan=2, padx=20, sticky=E)

        self.sel_neg_label = Label(
            self.frame_lefthalf,
            text="Selection Negative Ratings: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_neg_label.grid(column=0, row=5, padx=20, sticky=W)

        self.selectNegRat_label = Label(
            self.frame_lefthalf,
            text="select game for negative ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectNegRat_label.grid(column=1, row=5, columnspan=2, padx=20, sticky=E)

        self.gamescore_label = Label(
            self.frame_lefthalf,
            text="Selection game score",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.gamescore_label.grid(column=0, row=6, padx=20, sticky=W)

        self.selectgamescore_label = Label(
            self.frame_lefthalf,
            text="0/100",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectgamescore_label.grid(
            column=1, row=6, columnspan=2, padx=20, sticky=E
        )
        # Label van eerste spel in lijst:

        self.configurable_label = Label(
            self.frame_lefthalf,
            text="<<<click buttons on the left>>>",
            font=my_style_class.font_main,
            background=my_style_class.font_color,
            foreground=my_style_class.back_color,
        )
        self.configurable_label.grid(row=0, column=1, pady=20, padx=50, sticky="E")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # buttonframe for in lefttop frame
        self.button_frame = Frame(
            master=self.frame_lefthalf,
            bg="purple",
            relief=GROOVE,
            borderwidth=7,
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

        # *************************************************************************************************
        # Button to shutdown screen
        self.button_quit = Button(
            self.centeringframe,
            text="Quit Steam Dashboard",
            font=my_style_class.font_main,
            background="gray",
            foreground=my_style_class.font_color,
            cursor="cross",
            command=root.destroy,
        )
        self.button_quit.grid(column=1, row=7, sticky=E, padx=20)

        # Button to VirUSSsss
        self.button_donotpress = Button(
            self.centeringframe,
            text="DO NOT PRESS",
            font=my_style_class.font_main,
            background="red",
            highlightbackground="yellow",
            foreground="white",
            cursor="pirate",
            command=shutdowncommand,
        )
        self.button_donotpress.grid(column=0, row=7, padx=20, columnspan=2)

        # Button to open readme, also calls itself at start of programme after splash
        self.button_about = Button(
            self.centeringframe,
            text="About",
            font=my_style_class.font_main,
            background="gray",
            cursor="heart",
            fg=my_style_class.font_color,
            command=open_new_window_readme(),  # <--- TODO: change to open_new_window_readme() to auto start upon launch
        )
        self.button_about.grid(column=0, row=7, sticky=W, pady=10, padx=20)

        def selItemLabelChange():
            self.frame_lefthalf.sel_item_label["text"] = cur_treeview(a)[0]

        # *************************************************************************************************
        self.FIRE_LABEL = Label(
            root,
            text="loading ASCII",
            font=("TkFixedFont"),
            bg=my_style_class.back_color,
            fg="green",
        )

        self.FIRE_LABEL3 = Label(
            root,
            text="loading ASCII",
            font=("TkFixedFont"),
            bg=my_style_class.back_color,
            fg="green",
        )
        fire1 = glob.glob("lib/fire1.txt")
        fire2 = glob.glob("lib/fire2.txt")

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


def get_readme():
    all_readmes = glob.glob("README.md")
    # return first readme in list
    return open(all_readmes[0], "r", encoding="utf-8").read()


def open_new_window_readme():
    new_window = Toplevel()  # <---     open new window
    new_window.overrideredirect(True)  # <--- Removes Title bar

    # set the dimensions of the screen based upon earlier code
    # and where it is placed
    new_window.geometry("910x900")

    # Achtergrond kleur van de readme (inclusief transparency)
    new_window["bg"] = "black"
    new_window.wait_visibility(new_window)
    new_window.wm_attributes("-alpha", 0.99)

    # De data van de README.MD
    text = Text(
        new_window,
        width=120,
        height=53,
        font="TkFixedFont",
        fg="white",
        bg="black",
    )
    text.pack()  # <--- placement of .grid seperate or scrollbar doesnt compute
    text.insert(END, get_readme())

    # close readme
    Button(
        new_window, text="close", bg="red", command=new_window.destroy, width=100
    ).pack(padx=25, pady=10)


def shutdowncommand():
    root.destroy()

    gui = Tk()
    # set window size
    gui.wm_attributes(
        "-alpha", 1, "-fullscreen", True
    )  # <---waits, then makes page translucent and fullscreen
    gui["bg"] = "blue"
    count = 100

    countdown = Label(gui, text="SHUTDOWN IMMINENT", bg=None, font=("countdown", 40))
    countdown.pack(fill="both")

    img = Image.open("lib/virus.jpg")
    img2 = ImageTk.PhotoImage(img)
    img_label = Label(gui, image=img2, bg="blue")
    img_label.pack(fill="both", expand=True)
    gui.update_idletasks()  # <--- run configure task while still in loop !!!!

    warning = Label(gui, text="WARNING", bg=None, font=("countdown", 40))
    warning.pack(fill="both", side="bottom", pady=50)

    x = 0
    print(f"ok go{x}")
    count = 100

    while x < 100:
        if x % 8 == 0:
            countdown["bg"] = "red"
            countdown["text"] = f"WARNING: {count}"
            warning["text"] = f"~☠~☠~☠~☠~☠~"
            countdown["bg"] = "yellow"
            gui.update_idletasks()

        print(f"ok go{x}")
        count = count - 0.5
        countdown["text"] = f"WARNING: {count}"
        warning["text"] = f"SHUTDOWN IMMINENT"

        time.sleep(0.025)
        warning["fg"] = "red"

        gui.update_idletasks()
        time.sleep(0.025)
        x = x + 1
        count = count - 0.5

        cur_gui = "gui" + str(x)
        cur_gui = Toplevel()
        place = str(x * 20)
        place2 = "100x100+" + place + "+" + place
        cur_gui.geometry(place2)
        Label(cur_gui, text="☠", font=("verdana", 100)).pack()
        cur_gui.update_idletasks()  # <--- run configure task while still in loop !!!!

        cur_gui.mainloop

    gui.destroy()
    return



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


def gradenaanwijziging(
    percentage,
):  # Functie om de Servo te laten draaien naar likes percentage
    graden = percentage / 10 + 2
    print("error: ~~~~ goto line 430ish gradenaanwijzing() and uncomment")
    # pwm.ChangeDutyCycle(2)
    # sleep(0.1)
    # pwm.ChangeDutyCycle(graden)
    print(f"moving servo to {graden} degrees at percentage {percentage}")


# *************************************************************************************************
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
        # splash_label.configure(
        #     text=i
        # )  # <--- change bottom screen text each imagechange
        filename = i
        img_var = Image.open(filename)  # <--- load next image
        photo_image = ImageTk.PhotoImage(img_var)
        img_label.configure(image=photo_image)  # <--- swap current image with next
        splashscreen.update_idletasks()  # <--- run configure task while still in loop !!!!
        if i == 'steamlogolarge60.jpg':
            insert_alltime_games_page1()
        sleep(random.uniform(1, 1.5))


def delayed_start():
    if __name__=='__main__':
        Thread(target = change_label).start()
        time.sleep(3)
        Thread(target = API_PULL).start()



# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# initial fill splashscreen
from PIL import Image, ImageTk  # <--- leave in to ensure proper usage of PIL

img = Image.open("steamlogolarge40.jpg")
photoimage = ImageTk.PhotoImage(img)
img_label = Label(splashscreen, image=photoimage)
img_label.pack()
splash_label = Label(
    splashscreen, text="made by Ryan Reddy, Jeffrey Vizility, Tuur Neex219, Léon Phj1969, Souf", bg=my_style_class.back_color, fg="gold"
)
splash_label.pack()
# *************************************************************************************************
# API
def create():
    try:
        curs.execute(
            """CREATE TABLE IF NOT EXISTS games_alltime(
        app_id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        developer TEXT NOT NULL,
        positive INTEGER NOT NULL,
        negative INTEGER NOT NULL
        )"""
        )
    except:
        print('cant create')
        pass


def insert_alltime_games_page1():
    # TODO: make multiple inserts/databases: ---> https://steamspy.com/api.php

    url = "https://steamspy.com/api.php?request=all&page=0"
    data = requests.get(url).json()
    for game_id, game in data.items():  # <--- unpacks the dictionairy in dictionairy
        print(game)
        app_id = game.get("appid", "no_data")
        name = game.get(
            "name", "no_name_found"
        )  # <--- 'no_name_found' option as backup for .get
        developer = game.get("developer", "no_data")
        positive = game.get("positive", "no_data")
        negative = game.get("negative", "no_data")

        arguments = (
            app_id,
            name,
            developer,
            positive,
            negative,
        )

        splash_label.configure(
            text=arguments
        )  # <--- change bottom screen text each imagechange
        splashscreen.update_idletasks()  # <--- run configure task while still in loop !!!!

        try:
            curs.execute(
                """INSERT INTO games_alltime(
            app_id, 
            name, 
            developer, 
            positive, 
            negative) VALUES(?, ?, ?, ?, ?)""",
                arguments,
            )
        except:
            pass


def select():
    sql = "SELECT * FROM games_alltime"
    recs = curs.execute(sql)
    if True:
        for row in recs:
            print(row)


def API_PULL():
    conn = None
    conn = sqlite3.connect("lib/steam_database.db")
    curs = conn.cursor()
    create()
    insert_alltime_games_page1()
    conn.commit()  # <--- commit needed
    select()
    curs.close()
    if conn is not None:
        conn.close()

# *************************************************************************************************
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen programme:
splashscreen.after(
    12000,
    splashscreen.destroy,  # TODO <--- 12000ms set to 0 this one to skip splashscreen
)
# function should be "delayedstart":
splashscreen.after(2000, delayed_start)

splashscreen.eval("tk::PlaceWindow . center")  # <--- center splashscreen

splashscreen.mainloop()

# *************************************************************************************************
# TREEVIEW
root = Tk()
# window format:
root.eval("tk::PlaceWindow . center")  # <--- window to center screen
root.wait_visibility(root)  # <---waits, then makes page translucent
root.wm_attributes(
    "-alpha", my_style_class.window_transparency, "-fullscreen", True
)  # <---waits, then makes page translucent and fullscreen
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
_frame = Frame(root, background=treeview_style_class.back_color, relief="ridge")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def show_table():
    src_entry.delete(0, END)
    src_entry.focus()
    treeview.selection()
    conn = None

    try:
        conn = sqlite3.connect(database_filepath)
        curs = conn.cursor()
        curs.execute("SELECT * FROM games_alltime")

        fetchdata = treeview.get_children()
        for elements in fetchdata:
            treeview.delete(elements)

        data = curs.fetchall()
        for d in data:
            treeview.insert(
                "",
                END,
                values=d,
                tags="body",
            )

        conn.commit()
    except Exception as e:
        showerror("Fail", e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def getdata():
    print('letsgo')
    children = treeview.get_children()
    print(children)
    searchresults_json = open("lib/zoekresultaten.txt", 'w')  # <--- bereid een lege zoekresultaten.json voor
    for i in children:
        values = treeview.item(i)["values"]
        print(values)
        searchresults_json.write(values,'\n')
    searchresults_json.close
    print('closed file ~~~~~~~~~~~~~~~~~~~~~~')
    return

def search(event):
    # treeview.selection()
    fetchdata = treeview.get_children()
    for f in fetchdata:
        treeview.delete(f)
    conn = None
    try:
        conn = sqlite3.connect(database_filepath)
        curs = conn.cursor()
        name = src_entry.get()
        # <--- searches for arguments mentioned below
        if len(name) < 2:
            showerror("fail", "invalid name")
        else:
            wildcard = "%"
            arguments = (wildcard + name + wildcard,)
            curs.execute(
                """select * from games_alltime where (name || developer) LIKE ?""",
                (arguments),
            )
            data = curs.fetchall()
            for d in data:
                treeview.insert("", END, values=d, tags="body")
            treeview.tag_configure("body", background="black", foreground="green")
        getdata()

    # except Exception as e:
    #     showerror("issue", e)
    finally:
        if conn is not None:
            conn.close()


def sort_by(treeview, col, reverse):
    l = [(treeview.set(k, col), k) for k in treeview.get_children("")]
    print(l)
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        treeview.move(k, "", index)

    # reverse sort next time
    treeview.heading(col, command=lambda: sort_by(treeview, col, not reverse))


def reset():
    show_table()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Het json bestand uitlezen en opslaan als variable.
# data = open("zoekresultaten.txt")
# data = json.load(source)

# Functie voor berekenen gemiddelde prijs van alle games.
def average_game_price():
    with open('lib/zoekresultaten.txt') as f:
        lines = f.readlines()
        data = lines
        print(lines)
        print(type(data))
        print('partlyyyyy')
        print(data.split()[1])
        print('end')
    # Lees elk spel uit het bestand in en sla het aantal spellen en de totale prijs op.
    count = 0
    total = 0
    for i in data:
        count += 1
        total += int(i["price"])

    # Bepaal de gemiddelde prijs van alle spellen en geeft deze waarde terug als getal met 2 decimalen.
    average = total / count
    # average = "{:.2f}".format(total/count)
    formatting = "{average_price:.2f}"
    return formatting.format(average_price=average) # TODO implement this "quantitative variable" to mainscreen


# Functie voor ophalen van alle game developers.
def list_game_developers():


    return developers


# Functie voor ophalen van alle game developers.
def list_first_game_developers():
    searchresults_json = open("lib/zoekresultaten.txt", 'r')  # <--- bereid een lege zoekresultaten.json voor
    # Lees alle developers uit het bestand in en sla de namen op, geeft deze namen terug als resultaat.
    developers = []
    for i in searchresults_json:
        x = i
        print(type(x))
        print('hello',x)
        developers.append(x)
    # Lees de developer(s) uit het bestand in van de eerste game en sla deze op, geeft dit terug als resultaat.
    print(type(developers))
    print(developers)
    print('firsty')
    dev1 = developers[0]
    print(dev1)
    print(type(dev1))

    return dev1

def list_first_game():
    # Lees de developer(s) uit het bestand in van de eerste game en sla deze op, geeft dit terug als resultaat.
    x = data[0]
    game = x["name"]
    return game

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


treeview = ttk.Treeview(
    separator, columns=("#1", "#2", "#3", "#4", "#5"), show="headings", height=21
)  # <--- maakt treeview headings
treeview.grid()

treeview.heading("#1", text="Appid", command=lambda c="#1": sort_by(treeview, c, 0))
treeview.column("#1", minwidth=10, width=50, stretch=False)
treeview.heading("#2", text="Name", command=lambda c="#2": sort_by(treeview, c, 0))
treeview.column("#2", minwidth=10, width=220, stretch=False)
treeview.heading("#3", text="Developer", command=lambda c="#3": sort_by(treeview, c, 0))
treeview.column("#3", minwidth=10, width=120, stretch=False)
treeview.heading(
    "#4", text="Positive Ratings", command=lambda c="#4": sort_by(treeview, c, 0)
)
treeview.column("#4", stretch=YES, width=60)
treeview.heading(
    "#5", text="Negative Ratings", command=lambda c="#5": sort_by(treeview, c, 0)
)
treeview.column("#5", stretch=YES, width=50)
treeview.tag_configure(
    "body", background="black", foreground="green"
)  # <--- colors table body


style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
style.configure(
    "Treeview.Heading",
    rowheight=21,
    foreground="white",
    background=my_style_class.back_color,
)  # <--- creates the heading style

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# Creates the scrollbar:
xscrollbar = Scrollbar(separator, orient=HORIZONTAL, command=treeview.xview)
yscrollbar = Scrollbar(
    separator, orient=VERTICAL, command=treeview.yview, background="black"
)

# # Places the scrollbar
yscrollbar.grid(row=0, column=1, sticky=NS, pady=10, padx=(0, 10))
# xscrollbar.grid(row=1, column=0, sticky=EW)


def cur_treeview(a):

    curItem = treeview.focus()
    info_string = treeview.item(curItem)
    treeview.rowconfigure(treeview.index(curItem), minsize=15)

    # show selected info in buttons:
    total_info = info_string.get("values")
    positive_ratings = total_info[3]  # <--- assign
    negative_ratings = total_info[4]  # <--- assign
    symbol = "%"
    total_reviews = negative_ratings + positive_ratings
    percentage = round((positive_ratings / total_reviews) * 100)
    percentagelabeltekst = f"{percentage}{symbol}"
    score = f"SCORE: {percentage/10}/10"

    mainscreen.sel_item_label.config(text=total_info[1], anchor=E)
    mainscreen.selectPosRat_label.config(text=positive_ratings)
    mainscreen.selectNegRat_label.config(text=negative_ratings)

    mainscreen.configurable_label.config(text=score)
    mainscreen.selectgamescore_label.config(text=percentagelabeltekst, bg="green")

    gradenaanwijziging(percentage)  # <--- percentagecalc in action

    def ratings_calc(neg_reviews, pos_reviews):
        total_reviews = neg_reviews + pos_reviews
        percentage = round((pos_reviews / total_reviews) * 100, 2)
        gradenaanwijziging(percentage)
        return percentage

    ratings_calc(negative_ratings, negative_ratings)

    return


treeview.bind("<ButtonRelease-1>", cur_treeview)  # <--- grab data from clicked row


# *************************************************************************************************
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
database_filepath = "lib/steam_database.db"


ws_lbl = Label(
    mainscreen.button_frame,
    text="SEARCH:",
    font=("calibri", 12, "normal"),
    bg="black",
    fg="white",
)
ws_lbl.pack(pady=(20, 0))


src_entry = Entry(
    mainscreen.button_frame,
    bg=my_style_class.font_color,
    fg=my_style_class.back_color,
    font=("roboto", 10),
    width=30,
)

src_entry.insert(END, """Enter here...""")  # <--- standard text in entrybox
src_entry.pack(padx=20, pady=(20))
src_entry.bind("<Return>", search)  # <--- uses event"return"
src_entry.bind("<KP_Enter>", search)  # <--- uses event"numpad-enter"


src_button = Button(
    mainscreen.button_frame,
    text="Search",
    width=8,
    font=("calibri", 12, "normal"),
    bg="black",
    fg="white",
)
src_button.pack(side=LEFT)
src_button.bind(
    "<Button-1>", search
)  # <--- uses event "mousebutton-1 on src_button widget! cause: binding to <return>"

ws_btn2 = Button(
    mainscreen.button_frame,
    text="Reset",
    width=8,
    font=("calibri", 12, "normal"),
    command=reset,
    bg="black",
    fg="white",
)
ws_btn2.pack(side=RIGHT)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def clear_entrybox(event):  # <--- clear the entrybox upon click
    src_entry.delete(0, "end")
    return None


src_entry.bind(
    "<Button-1>", clear_entrybox
)  # <--- binds mousebutton1 click to clear_entrybox


# *************************************************************************************************

show_table()

# *************************************************************************************************

""" Run main GUI"""

root.mainloop()

# *************************************************************************************************
# servo afsluiting
pwm.stop()  # moet na de .mainloop
GPIO.cleanup()
