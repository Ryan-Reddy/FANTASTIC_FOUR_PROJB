"""
//=============================================================================
//  GUI of the Application
//=============================================================================
"""
# import glob
from time import sleep
import random
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *
import time
import sqlite3
import json
import requests
from PIL import Image, ImageTk  # <--- leave in to ensure proper usage of PIL

# TODO: RASPBERRY PI  get a working gpio rpio package > then uncomment:
# import RPi.GPIO as GPIO     # nodig voor Servo
"""
//=============================================================================
//  Tkinter style/GUI classes
//=============================================================================
Set these up for overview, and to have the style at the start of document before the functions.
"""


class StyleClass:
    """
    basic styleclass for the entire GUI
    """
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


my_style_class = StyleClass(
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

treeview_style_class = StyleClass(
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
    """ Center frame size as a class
    """
    def __init__(self, width, height, count):
        self.width = width
        self.height = height
        self.count = count
center_frame_class = FrameSize(1200, 600, 0)


class MainScreen:
    """Mainscreen class with buttons and functions
    """
    def destuction_imminent(self):
        shutdowncommand

    def button1game(self):
        self.configurable_label.config(text=list_first_game())

    # def button2(self):
    #     self.configurable_label.config(
    #         text=average_game_price(),
    #     )

    def button3(self):
        self.configurable_label.config(text=first_gameDev_inlist())

    def button4(self):
        self.configurable_label.config(text=avg_pos_game_rating())

    def button5(self):
        self.configurable_label.config(text=avg_neg_game_rating())

    def button6(self):
        self.configurable_label.config(text=avg_gamescore())

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
        """ *************************************************************************************
        //  Onscreen labels
        //  *************************************************************************************"""
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

        self.selectposrat_label = Label(
            self.frame_lefthalf,
            text="click on a game for positive ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectposrat_label.grid(column=1, row=4, columnspan=2, padx=20, sticky=E)

        self.sel_neg_label = Label(
            self.frame_lefthalf,
            text="Selection Negative Ratings: ",
            font=my_style_class.font_main,
            background="green",
            fg=my_style_class.font_color,
        )
        self.sel_neg_label.grid(column=0, row=5, padx=20, sticky=W)

        self.selectnegrat_label = Label(
            self.frame_lefthalf,
            text="select game for negative ratings",
            font=my_style_class.font_main,
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
        )
        self.selectnegrat_label.grid(column=1, row=5, columnspan=2, padx=20, sticky=E)

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
        """ *************************************************************************************
        //  Left top frame and buttons
        //  *************************************************************************************"""
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
            text="Top search result",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button1game,
            font=("roboto", 10),
            width=30,
            cursor="target",
        )
        self.button.pack()

        # self.button2 = Button(
        #     master=self.button_frame,
        #     text="average_game_price",
        #     bg=my_style_class.back_color,
        #     fg=my_style_class.font_color,
        #     command=self.button2,
        #     font=("roboto", 10),
        #     width=30,
        #     cursor="exchange",
        # )
        # self.button2.pack()

        self.button3 = Button(
            master=self.button_frame,
            text="Top game developer",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button3,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button3.pack()

        self.button4 = Button(
            master=self.button_frame,
            text="Average Positive ratings",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button4,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button4.pack()

        self.button5 = Button(
            master=self.button_frame,
            text="Average Negative ratings",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button5,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button5.pack()

        self.button6 = Button(
            master=self.button_frame,
            text="Average Gamescore results",
            bg=my_style_class.back_color,
            fg=my_style_class.font_color,
            command=self.button6,
            font=("roboto", 10),
            width=30,
            cursor="man",
        )
        self.button6.pack()
        """ *************************************************************************************
        //  Bottom of screen buttons
        //  *************************************************************************************"""
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
            command=open_new_window_readme()
            or open_new_window_readme,  # <--- added "()" to auto start upon launch
        )
        self.button_about.grid(column=0, row=7, sticky=W, pady=10, padx=20)

        # def selItemLabelChange():
        #     self.frame_lefthalf.sel_item_label["text"] = cur_treeview(a)[0]
        """ *************************************************************************************
        //  FIRE ASCII animation
        //  *************************************************************************************
        Self built ASCII animation, based upon an image turned ASCII
        mirrored the two, and built a little loop that constantly alternates between the two"""
        self.fire_label = Label(
            root,
            text="loading ASCII",
            font="TkFixedFont",
            bg=my_style_class.back_color,
            fg="green",
        )
        self.fire_label2 = Label(
            root,
            text="loading ASCII",
            font=("TkFixedFont"),
            bg=my_style_class.back_color,
            fg="green",
        )

        def get_txt1():
            """Grabs ASCII for first flame
            :return: text as string
            """
            text1 = open("fire1.txt", "r", encoding="utf-8").read()
            return text1

        def get_txt2():
            """Grabs ASCII for second flame
            :return: text as string
            """
            text2 = open("fire2.txt", "r", encoding="utf-8").read()
            return text2

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # FIRE programma zelf

        def moving_ascii():
            """Flame one direction.
            :return: None
            """
            self.fire_label.configure(text=get_txt1())
            self.fire_label2.configure(text=get_txt1())
            self.fire_label.after(my_style_class.flame_speed, moving_ascii2)

        def moving_ascii2():
            """Flame other direction.
            :return: None
            """
            self.fire_label.configure(text=get_txt2())
            self.fire_label2.configure(text=get_txt2())
            self.fire_label.after(my_style_class.flame_speed, moving_ascii)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # PLaatsting FIRE
        self.fire_label.place(relx=0.25, rely=1, anchor=S)
        self.fire_label2.place(relx=0.75, rely=1, anchor=S)
        self.fire_label.after(1, moving_ascii)
        self.fire_label2.after(1, moving_ascii)


"""
//=============================================================================
//  Readme launcher
//=============================================================================
get_readme:                 Grabs the readme from the projectfolder
open_new_window_readme:     runs a new tkinter window with readme data
"""


def get_readme():
    """Grabs readme file
    :return: readme as string
    """
    return open("README.md", "r", encoding="utf-8").read()


def open_new_window_readme():
    """Opens a new window and displays readme with ASCII correctly
    :return: None
    """
    new_window = Toplevel()  # <---     open new window
    # new_window.overrideredirect(True)  # <--- Removes Title bar
    new_window.geometry("910x900")
    new_window["bg"] = "black"
    new_window.wait_visibility(new_window)
    new_window.wm_attributes("-alpha", 0.99)  # <--- Transparency readme

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


"""
//=============================================================================
//  Do-not-press programme (virus)
//=============================================================================
Little easter egg
"""


def shutdowncommand():
    """runs a basic countdown timer that updates screen
    :return: destroys GUI
    """
    root.destroy()

    gui = Tk()
    # set window size
    gui.wm_attributes(
        "-alpha", 1, "-fullscreen", True
    )  # <---waits, then makes page translucent and fullscreen
    gui["bg"] = "blue"
    count = 100

    countdown = Label(gui, text="SHUTDOWN IMMINENT", font=("countdown", 40))
    countdown.pack(fill="both")
    virus_image = Image.open("virus.jpg")
    virus_image_tk = ImageTk.PhotoImage(virus_image)
    virus_image_label = Label(gui, image=virus_image_tk, bg="blue")
    virus_image_label.pack(fill="both", expand=True)
    gui.update_idletasks()  # <--- run configure task while still in loop !!!!
    warning = Label(gui, text="WARNING", font=("countdown", 40))
    warning.pack(fill="both", side="bottom", pady=50)

    x = 0
    count = 100
    while x < 100:
        if x % 8 == 0:
            countdown["bg"] = "red"
            countdown["text"] = f"WARNING: {count}"
            warning["text"] = "~☠~☠~☠~☠~☠~"
            countdown["bg"] = "yellow"
            gui.update_idletasks()

        count = count - 0.5  # <--- onscreen countdown speed
        countdown["text"] = f"WARNING: {count}"
        warning["text"] = "SHUTDOWN IMMINENT"

        time.sleep(0.025)  # <--- actual countdown speed
        warning["fg"] = "red"

        gui.update_idletasks()
        time.sleep(0.025)  # <--- actual countdown speed
        x = x + 1
        count = count - 0.5
        cur_gui = Toplevel()
        place = str(x * 20)
        place2 = "100x100+" + place + "+" + place
        cur_gui.geometry(place2)
        popup = Label(cur_gui, text="☠", font=("TkFixedFont", 100))
        popup.pack()
    return gui.destroy()


"""
//=============================================================================
//  Review-O-Meter 2000 (review-score-servo)
//=============================================================================
"""
# # # TODO: uncomment after installing on pi with package:
# # GPIO.setmode(GPIO.BCM)        # Alles hierin nodig voor Servo
# #GPIO.setup(18, GPIO.OUT)    # Servo op ping 18
# # pwm=GPIO.PWM(18, 50)            # zit op pin 18, 50 hz
# # pwm.start(1)
# # raspberry PI function to control servo


def gradenaanwijziging(
    percentage,
):
    """
    function to change position servo based upon input
    :param percentage: a number between 0-100
    :return: sends a signal to the GPIO
    """

    graden = percentage / 10 + 2
    print("error: ~~~~ goto line 430ish gradenaanwijzing() and uncomment")
    # pwm.ChangeDutyCycle(2)
    # sleep(0.1)
    # pwm.ChangeDutyCycle(graden)
    print(f"moving servo to {graden} degrees at percentage {percentage}")


gradenaanwijziging(50)  # <--- keeps servo quiet till command

"""
//=============================================================================
//  SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme
//=============================================================================
Basic set up of splashscreen
"""
splashscreen = Tk()  # <--- setup splashscreen
splashscreen.overrideredirect(True)  # <--- Removes titlebar
splashscreen.call("wm", "attributes", ".", "-topmost", "true")  # <--- topmost screen
splashscreen.geometry(
    "965x337"
)  # <--- # size of screen + positie (steam-logo-large.jpg = 960x307)
splashscreen["bg"] = my_style_class.back_color  # <--- background colour splash


def change_label():
    """
    Runs through a list to change loading image
    :return: None
    """
    splashpath = "splash.txt"
    with open(splashpath, encoding="utf-8") as splash_loader_filelist:
        splash_order = splash_loader_filelist.read().splitlines()
        splash_loader_filelist.close()
    for i in splash_order:
        # splash_label.configure(
        #     text=i
        # )  # <--- change bottom screen text each imagechange
        filename = i
        img_var = Image.open(filename)  # <--- load next image
        photo_image = ImageTk.PhotoImage(img_var)
        img_label.configure(image=photo_image)  # <--- swap current image with next
        splashscreen.update_idletasks()  # <--- run configure task while still in loop !!!!
        if i == "steamlogolarge60.jpg":
            insert_alltime_games_page1()
        sleep(random.uniform(1, 1.5))


def delayed_start():
    """
    Basic splashscreen programme (.after to update tkinter while running)
    :return: None
    """
    if __name__ == "__main__":
        # Thread(target = change_label).start()
        # Thread(target=API_PULL).start()
        API_PULL()
        change_label()


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
# initial filling splashscreen

img = Image.open("steamlogolarge40.jpg")
photoimage = ImageTk.PhotoImage(img)
img_label = Label(splashscreen, image=photoimage)
img_label.pack()
splash_label = Label(
    splashscreen,
    text="made by Ryan Reddy, Jeffrey Vizility, Tuur Neex219, Léon Phj1969, Souf",
    bg=my_style_class.back_color,
    fg="gold",
)
splash_label.pack()
"""
//=============================================================================
//  API pulling programme
//=============================================================================
"""


def create():
    """
    Creates a database, if exists, then pass
    :return: None
    """
    try:
        conn = sqlite3.connect("steam_database.db")
        curs = conn.cursor()
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
        print("Table exists- cant create")
        pass


def insert_alltime_games_page1():
    """
    requests data from API and INSERTS this into a SQL
    :return: None
    """
    url = "https://steamspy.com/api.php?request=all&page=0"
    api_data = requests.get(url).json()
    for game_id, game in api_data.items():  # <--- unpacks the dictionairy in dictionairy
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
        )  # <--- change bottom screen text each api line request
        splashscreen.update_idletasks()  # <--- run configure task while still in loop !!!!

        try:
            conn = sqlite3.connect("steam_database.db")
            curs = conn.cursor()
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


def API_PULL():
    """
    loop to run through an api pull and message into splash
    :return: None
    """
    conn = None
    conn = sqlite3.connect("steam_database.db")
    curs = conn.cursor()
    create()
    insert_alltime_games_page1()
    splash_label.configure(
        text="made by Ryan Reddy, Jeffrey Vizility, Tuur Neex219, Léon Phj1969, Souf with love ~~~",
        bg=my_style_class.back_color,
        fg="white",
    )
    conn.commit()  # <--- commit needed
    # select()
    curs.close()
    if conn is not None:
        conn.close()


"""
//=============================================================================
//  splashscreen programme:
//=============================================================================
This loading screen, keeps the user entertained while retrieving data from steamspyAPI"""

splashscreen.after(
    10000,  # <--- ending timer for splashscreen in ms
    splashscreen.destroy,
)
splashscreen.after(10, delayed_start)
splashscreen.eval("tk::PlaceWindow . center")  # <--- center splashscreen
splashscreen.mainloop()

"""
//=============================================================================
//  Database functions - Search in database - show in treeview
//=============================================================================
"""


def show_table():
    """shows the database that was built from the api request
    :return: None
    """
    src_entry.delete(0, END)
    src_entry.focus()
    treeview.selection()
    conn = None

    try:
        conn = sqlite3.connect(DATABASE_FILEPATH)
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


def write_searchresults(data):
    """Clears old searchresults and stores search results in a *.json, for use in the AI search functions.
    :param data: data
    :return: None
    """
    children = treeview.get_children()
    searchresults_json = open("searchresults.json", "w")
    for i in children:
        values = treeview.item(i)["values"]
    searchresults_json.write(json.dumps(data, indent=4))

    searchresults_json.close


def search(event):
    """Searches in the DB using user input and SQL query
    :param event: Filled in entrybox and pressed<enter>/clicked<searchbutton>
    :return: None
    """
    fetchdata = treeview.get_children()
    for f in fetchdata:
        treeview.delete(f)
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILEPATH)
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
            write_searchresults(data)  # <--- saves search res. in .sjon
    except Exception as e:
        showerror("issue", e)
    finally:
        if conn is not None:
            conn.close()


def sort_by(treeview, col, reverse):
    """Sorts data based on alphabetical or numeric order
    :param treeview:        {set, get_children, move, heading}
    :param col:             column name
    :param reverse:         reverse order or not
    :return:                None
    """

    l = [
        (treeview.set(k, col), k) for k in treeview.get_children("")
    ]  # <--- grabs columnvalues and titles
    print(l)
    l.sort(reverse=reverse)  # <--- uses treeview.sort

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        treeview.move(k, "", index)

    # reverse sort next time
    treeview.heading(col, command=lambda: sort_by(treeview, col, not reverse))


def reset():
    """Resets table to pre-search status
    :return: None
    """
    show_table()


"""
//=============================================================================
//  Treeview programme:
//=============================================================================
"""

root = Tk()
# window format:
# root.eval("tk::PlaceWindow . center")  # <--- window to center screen
root.wait_visibility(root)  # <---waits, then makes page translucent
root.wm_attributes(
    "-alpha", my_style_class.window_transparency, "-fullscreen", True
)  # <---waits, then makes page translucent and fullscreen
root.configure(background=my_style_class.back_color)
mainscreen = MainScreen(root)
"""
//=============================================================================
//  TREEVIEW ~ window, style, data, scrollbar, column-sorting-function
//=============================================================================
"""
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

DATABASE_FILEPATH = "steam_database.db"

"""
//=============================================================================
//  Search function Tkinter layout
//=============================================================================
"""

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


def clear_entrybox(event):  # <---
    """clear the entrybox upon click
    :param event: mouseclick upon entrybox
    :return: None
    """
    src_entry.delete(0, "end")


src_entry.bind("<Button-1>", clear_entrybox)  # <--- empties entrybox upon mouseclick
"""
//=============================================================================
//  AI search functions
//=============================================================================
"""


def get_lastsearch():
    """Grabs the data from the last search saved remotely as json
    :return: data as json object
    """
    source = open("searchresults.json")
    data = json.load(source)
    return data


def list_first_game():
    """Picks first game in search results
    :return: First game-title as string
    """
    data = get_lastsearch()
    x = data[0]
    game = x[1]
    return game


def list_game_developers():
    """Lists all game devs from last search, returns names as a list.
    :return: a list object
    """
    developers = []
    data = get_lastsearch()
    for i in data:
        x = str(i[2])
        developers.append(x)
    return developers


def first_gameDev_inlist():
    """calls list_game_developers, returns first developer as string
    :return:  a string object
    """
    data = list_game_developers()
    first_developers = data[0]
    return first_developers


def avg_pos_game_rating():
    """Calculates average positive game ratings of last search
    :return: An integer
    """
    data = get_lastsearch()
    game_count = 0
    total_positive_ratings = 0
    for i in data:
        game_count += 1
        total_positive_ratings += int(i[3])
    average = total_positive_ratings / game_count
    formatting = "{average_positive_rating:.0f}"
    return formatting.format(average_positive_rating=average)


def avg_neg_game_rating():
    """Calculates average negative game ratings of last search
    :return: an integer
    """
    data = get_lastsearch()
    game_count = 0
    total_negative_ratings = 0
    for i in data:
        game_count += 1
        total_negative_ratings += int(i[4])
    average = total_negative_ratings / game_count
    formatting = "{average_negative_rating:.0f}"
    return formatting.format(average_negative_rating=average)


def avg_gamescore():
    """Calculates average game score of last search
    :return: an integer between 0-100
    """
    positivo = int(avg_pos_game_rating())
    negativo = int(avg_neg_game_rating())
    totalito = positivo + negativo
    factorito = (positivo / totalito) * 100
    total = round(factorito)
    return total


""" //=============================================================================
    //  TREEVIEW ~ Data insert, styles
    //============================================================================="""
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

"""
//=============================================================================
//  TREEVIEW ~ grab current selection
//=============================================================================
"""


def cur_treeview(a):
    """Grabs data from selected row in treeview
    :param a: a placeholder (useless)
    :return: None
    """
    Cur_Item = treeview.focus()
    info_string = treeview.item(Cur_Item)

    if len(Cur_Item) == 0:  # <--- skips headerclicks
        return
    if len(Cur_Item) != 0:
        treeview.rowconfigure(treeview.index(Cur_Item), minsize=115)
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
        mainscreen.selectposrat_label.config(text=positive_ratings)
        mainscreen.selectnegrat_label.config(text=negative_ratings)

        mainscreen.configurable_label.config(text=score)
        mainscreen.selectgamescore_label.config(text=percentagelabeltekst, bg="green")

        def ratings_calc(neg_reviews, pos_reviews):
            """
            Calculates
            :param neg_reviews: Total negative reviews of selection
            :param pos_reviews: Total positive reviews of selection
            :return: Float rounded on 2 decimals
            """
            total_reviews = neg_reviews + pos_reviews
            percentage = round((pos_reviews / total_reviews) * 100, 2)
            gradenaanwijziging(percentage)
            return percentage

        ratings_calc(negative_ratings, negative_ratings)


treeview.bind("<ButtonRelease-1>", cur_treeview)  # <--- grab data from clicked row

"""
//=============================================================================
//  GUI - main programme
//=============================================================================
"""
data = [
    ["Search first!", "I need some data!", "Search first!", 69, 420],
] * 5
write_searchresults(data)  # <--- saves an empty search res. in .sjon before start

show_table()  # <--- grabs data from the sql for in treeview
root.mainloop()
pwm.stop()  # must be after mainloop
GPIO.cleanup()
