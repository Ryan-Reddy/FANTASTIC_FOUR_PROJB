from tkinter import *
import time
# from testing_new_GUI import *
from PIL import Image, ImageTk
import os


def open_new_window_readme():
    new_window = Toplevel()  # <---     open new window
    new_window.overrideredirect(True)  # <--- Removes Title bar

    # set the dimensions of the screen based upon earlier code
    # and where it is placed
    new_window.geometry("860x875")

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
    Button(new_window, text="close", bg="red", command=new_window.destroy, width=100).pack(padx=25, pady=10
    )


def shutdowncommand():
    gui = Tk()
    # set window size
    gui.wm_attributes("-alpha", 1, "-fullscreen", True)  # <---waits, then makes page translucent and fullscreen
    gui['bg'] = 'black'
    count = 100

    countdown = Label(gui, text="SHUTDOWN IMMINENT", bg=None, font=('countdown', 40))
    countdown.pack(fill='both')

    img = PhotoImage("virus.jpg")
    img2 = PhotoImage(img)
    img_label = Label(gui, image=img)
    img_label.pack()

    warning = Label(gui, text='WARNING', bg=None, font=('countdown', 40))
    warning.pack(fill='both', side='bottom', pady=50)

    x =0
    print(f'ok go{x}')
    count = 100
    # gui['bg'] = 'yellow'
    time.sleep(3)

    while x < 50:
        if x%8==0:
            countdown['bg'] = 'red'
            countdown['text'] = f'WARNING: {count}'
            warning['text'] = f'~☠~☠~☠~☠~☠~'
            countdown['bg'] = 'yellow'
            gui.update_idletasks()

        print(f'ok go{x}')
        count = count-1
        countdown['text']=f'WARNING: {count}'
        warning['text']=f'SHUTDOWN IMMINENT'

        time.sleep(.05)
        warning['fg'] = 'red'

        gui.update_idletasks()
        time.sleep(.05)
        x = x+1
        count = count-1



        cur_gui = "gui"+str(x)
        cur_gui = Toplevel()
        place= str(x * 20)
        place2= "100x100+"+place+"+"+place
        cur_gui.geometry(place2)
        Label(cur_gui, text='☠',font=('verdana',100)).pack()

        cur_gui.mainloop

    # gui.after(1000, shutdowncommand)
    gui.destroy()
    cur_gui.destroy()
    return open_new_window_readme

    # gui.mainloop()
shutdowncommand()