"""Gui van de applicatie"""

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
back_color = 'black'
font_color = 'white'
# Steam logo font FF Din OT Bold:
font_choice_logo = ('FF Din OT', 14, 'bold')
font_choice = ('Arial'or'Helvetica', 12)
transparency = 0.8                              # <--- transparency mainscreen
theme = 'classic'                # <--- Change default to whichever theme you want to use.
# main_GUI_size = "" zodat deze aanpast aan de widgets die ik erin probeer te passen
raam_formaat = ""
# ******************************************************************************************************************
# TODO: change changeable text at bottom to commits, last minute change
"""# SPLASHSCREEN ~ setup, load list, motion seq., initial fill, main programme"""
# setup splashscreen
splashscreen = Tk()
# change window attributes
# Removes TITELBALK
splashscreen.overrideredirect(1)
# topmost screen
splashscreen.call('wm', 'attributes', '.', '-topmost', 'true')
# maat van screen + positie (steam-logo-large.jpg = 960x307)
splashscreen.geometry("960x307+471+387")
splashscreen.geometry('')
# Achtergrond kleur van de readme (inclusief transparency)
splashscreen['bg'] = back_color
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# load splashscreen picture order file:
with open(r"splashscreen\splash.txt") as l:
    print(l)
    splash_order = l.read().splitlines()
    l.close()
print(splash_order)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen IMAGER/motion sequence:
def change_label():
        Slabel.configure(text='sdasdasdasd')
        for i in splash_order:
            Slabel.configure(text=i)                    # <--- change bottom screen text each imagechange
            filename = i
            img = Image.open(filename)                  # <--- load next image
            ph = ImageTk.PhotoImage(img)
            img_label.configure(image=ph)               # <--- swap current image with next
            splashscreen.update_idletasks()             # <--- run configure task while still in loop !!!!
            time.sleep(random.uniform(1, 2.2))

def delayedstart():
    change_label()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# initial fill splashscreen
img = Image.open(splash_order[0])
ph = ImageTk.PhotoImage(img)
img_label = Label(splashscreen, image=ph)
img_label.pack()
Slabel = Label(splashscreen, text='loading', bg=back_color, fg='gold')
Slabel.pack()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# splashscreen programme:
"""set to 0 this one to skip splashscreen"""
splashscreen.after(00, splashscreen.destroy) #~12000ms
# function should be "delayedstart":
# splashscreen.after(2000, delayedstart)
splashscreen.after(0, print('startingsplashscreen'))

splashscreen.mainloop()
# ******************************************************************************************************************
""" README SCHERM GUI:"""
def open_new_window_readme():
    new_window = Toplevel(root)                                 # <---     open new window
    new_window.title("READ ME PLEASE")                          # <---     sets the title readme

    #Achtergrond kleur van de readme (inclusief transparency)
    new_window['bg'] = back_color
    new_window.wait_visibility(new_window)
    new_window.wm_attributes('-alpha', .99)
    # De data van de README.MD
    text = Text(new_window, width=120, height=40, font='TkFixedFont', fg=font_color, bg=back_color,)
    # plaatsen van grid (moet apart anders herkent de scrollbar m niet)
    text.grid(row=0)
    text.insert(END, get_readme())

    # Scrollbar
    scrollbar = ttk.Scrollbar(new_window, orient='vertical', command=text.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    # Readme scrollbar style
    style = ttk.Style()
    style.configure("Vertical.TScrollbar", background="black", bordercolor="black", arrowcolor="white")

    # knop sluit de newwindow af
    Button(new_window, text="Back", bg='red', command=new_window.destroy).grid(row=1)
# ******************************************************************************************************************
"""# MAINSCREEN ~ GUI settings:"""
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
# ******************************************************************************************************************
"""# MAINSCREEN ~ Labels and Buttons:"""

# De labels die je ziet op scherm
# TITEL
Label(root, text="Steam APP Fantastic Five", font=font_choice_logo, background=back_color,
      foreground=font_color, anchor=N, justify=CENTER).grid(column=1, row=0)

# Label van eerste spel in lijst:
Label(root, text="First game in list:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=0, row=1)
Label(root, text=first_game_in_json, font=font_choice, background='yellow',
      foreground='black').grid(column=3, row=1)

# label van gemiddelde prijs van de games:
Label(root, text="Average game price:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=0, row=2)
Label(root, text=average_game_price(), font=font_choice, background='yellow',
      foreground='black').grid(column=3, row=2)

# Label van eerste game dev in de lijst:
Label(root, text="First game developer:", font=font_choice, background=back_color,
      foreground=font_color).grid(column=0, row=3)
Label(root, text=list_first_game_developers(), font=font_choice, background='yellow',
      foreground='black').grid(column=3, row=3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Knoppen in mainscreen
# Knop om hoofdprogramma te eindigen
Button(root, text="Quit Steam Dashboard", font=font_choice, background='red', foreground=font_color,
       command=root.destroy).grid(column=0, row=6)

# Knop voor about(readme.md) in een apart scherm ~ start ook bij opstarten programma, vandaar  "" OR ""(self)
Button(root, text="About", font=font_choice, background='gray', foreground=font_color,
       command=open_new_window_readme or open_new_window_readme).grid(column=3, row=6)
# knop om te sorteren
# ******************************************************************************************************************
"""# TREEVIEW ~ window, stijl, data, scrollbar, kolomsorteerfunctie, """
# Maakt een raamwerk in de root aan voor de tabel

separator = PanedWindow(root, bd=0, bg=back_color, sashwidth=2)
separator.grid(column=1, row=5)
# rechter onderhoekje:
_frame = Frame(root, background=back_color, relief='ridge')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stijlen van de Tabel treeview:
style = ttk.Style()
style.theme_use('classic')
# style.configure("Treeview.Scrollbar", foreground='red', background=back_color)
style.configure("Treeview.Heading", foreground='green', background=back_color)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Geeft aan welke data uit de dictionairy mee te nemen
treeview = ttk.Treeview(root, show="headings",
                        columns=("Name", "Developer", "Platforms", "Genre"), style="Treeview.Heading")

# Voegt Kolomkoppen toe, command = sorteerfunctie(sortby)
treeview.heading("#1", text="Name", command=lambda c="#1": sortby(treeview, c, 0))
treeview.heading("#2", text="Developer", command=lambda c="#2": sortby(treeview, c, 0))
treeview.heading("#3", text="Platforms", command=lambda c="#3": sortby(treeview, c, 0))
treeview.heading("#4", text="Genre", command=lambda c="#4": sortby(treeview, c, 0))


# Plaatst data van data_import(main) in treeview tabel
# Plaatst ook tag = 'body' om later stijl toe te voegen
for row in data_import:
    treeview.insert("", "end", values=(row["name"], row["developer"], row["platforms"], row["genres"]), tags = 'body')
# stijlchoice body text
treeview.tag_configure('body', background=back_color)

# Geeft aan waar de tabel in het grid moet
treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sorteert columns naar klik op de headers TODO implementeer slimmere algoritmes
def sortby(tree, col, descending):
    # grab values to sort
    data = [(tree.set(child, col), child)
            for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
                                                     int(not descending)))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SCROLLBAR van tabel
ysb = ttk.Scrollbar(orient=VERTICAL, command=treeview.yview)
xsb = ttk.Scrollbar(orient=HORIZONTAL, command=treeview.xview)
treeview['yscroll'] = ysb.set
treeview['xscroll'] = xsb.set
separator.add(_frame)

# plaatst de scrollbar
ysb.grid(in_=_frame, row=0, column=1, sticky=NS)
xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
_frame.rowconfigure(0, weight=1)
_frame.columnconfigure(0, weight=1)
# attempt to color scrollbar

style.configure("Vertical.TScrollbar", background="black", bordercolor="black", troughcolor='black', highlightcolor='white')
style.configure("Horizontal.TScrollbar", background="black", bordercolor="black", troughcolor='black', highlightcolor='white')

# ******************************************************************************************************************
"""# FIRE ~setup, programma, plaatsing"""
# setup
Flabel = Label(root, text='a', font='TkFixedFont', bg='black', fg='gold')
def get_txt1():
    fire1= glob.glob("fire1.txt")
    return open(fire1[0], 'r', encoding='utf-8').read()

def get_txt2():
    fire2= glob.glob("fire2.txt")
    return open(fire2[0], 'r', encoding='utf-8').read()

text1= get_txt1()
text2= get_txt2()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIRE programma zelf

def moving_ascii():
    Flabel.configure(text=text1)
    print(root.geometry())
    Flabel.after(512, moving_ascii2)


def moving_ascii2():
    Flabel.configure(text=text2)
    print(root.geometry())
    Flabel.after(512, moving_ascii)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLaatsting FIRE
Flabel.grid(column=1, row=7)
Flabel.after(1, moving_ascii)
# ******************************************************************************************************************
"""# Running main GUI"""
root.mainloop()
# ******************************************************************************************************************




