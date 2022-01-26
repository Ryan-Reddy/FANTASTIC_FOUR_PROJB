from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *
import json

ws = Tk()
ws.title("Python Guides")
ws.geometry("750x700+400+50")
ws.resizable(0, 0)
ws.configure(bg="black")
# view_window
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# conn = None
# conn = connect("steam1.db")
# curs = conn.cursor()

# PRIMARY KEY (add to rno)
# curs.execute("""CREATE TABLE IF NOT EXISTS games(rno INTEGER PRIMARY KEY, app_id INTEGER NOT NULL, name TEXT NOT NULL)""")

# if conn is not None:
#     conn.close()
#
# conn = None
#
# conn = connect("steam1.db")
#
# curs = conn.cursor()

DATABASE_STEAM = "steam.json"
f = open(DATABASE_STEAM)
data_tree = json.load(f)
data_import = []
for line in data_tree:
    data_import.append(line)
number =0
for row in data_import:
    appid = row['appid']
    print(row)
    name = row['name']
    print(row['name'])
    query1 = "insert into games(appid,name) values(appid, name)"
    curs.execute(query1)


conn.commit()

if conn is not None:
    conn.close()


def show_table():
    ws_ent.delete(0, END)
    ws_ent.focus()
    treeview.selection()
    conn = None
    try:
        conn = connect("steam1.db")
        cursor = conn.cursor()
        db = "select * from games"
        cursor.execute(db)

        fetchdata = treeview.get_children()
        for elements in fetchdata:
            treeview.delete(elements)

        data = cursor.fetchall()
        for d in data:
            treeview.insert("", END, values=d,
        tags="body",)

        conn.commit()
    except Exception as e:
        showerror("Fail", e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def search():
    treeview.selection()
    fetchdata = treeview.get_children()
    for f in fetchdata:
        treeview.delete(f)
    conn = None
    try:
        conn = connect("steam1.db")
        core = conn.cursor()
        db = "select * from games where name = '%s' "
        name = ws_ent.get()
        if (len(name) < 2) or (not name.isalpha()):
            showerror("fail", "invalid name")
        else:
            core.execute(db % (name))
            data = core.fetchall()
            for d in data:
                treeview.insert("", END, values=d)

    except Exception as e:
        showerror("issue", e)

    finally:
        if conn is not None:
            conn.close()


def reset():
    show_table()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


treeview = ttk.Treeview(ws, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#3"), show='headings', height=21)
treeview.pack()


# Voegt Kolommen met settings toe, command = sorteerfunctie(sortby)
treeview.heading("#0", text="Appid", command=lambda c="#0": sort_by(treeview, c, 0))
treeview.column("#0", minwidth=10, width=50, stretch=0)
treeview.heading("#1", text="Name", command=lambda c="#1": sort_by(treeview, c, 0))
treeview.column("#1", minwidth=10, width=50, stretch=0)
treeview.heading("#2", text="Developer", command=lambda c="#2": sort_by(treeview, c, 0))
treeview.column("#2", stretch=YES, minwidth=50)
treeview.heading("#3", text="Platforms", command=lambda c="#3": sort_by(treeview, c, 0))
treeview.column("#3", stretch=YES, width=50)

treeview.heading("#4", text="Genre", command=lambda c="#4": sort_by(treeview, c, 0))
treeview.column("#4", stretch=YES, width=50)

treeview.heading("#5", text="Positive Ratings", command=lambda c="#5": sort_by(treeview, c, 0))
treeview.column("#5", stretch=YES, width=50)

treeview.heading("#6", text="Required Age", command=lambda c="#6": sort_by(treeview, c, 0))
treeview.column("#6", stretch=YES, width=50)

treeview.heading("#7", text="Publisher", command=lambda c="#7": sort_by(treeview, c, 0))
treeview.column("#7", stretch=YES, width=50)

treeview.heading("#8", text="Negative Ratings", command=lambda c="#8": sort_by(treeview, c, 0))
treeview.column("#8", stretch=YES, width=20)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
style.configure(
    "Treeview.Heading",
    rowheight=21,
    foreground= "white",
    background="black",
)  # <--- creates the basic table style

style.map(
    "Treeview.Heading",
    background=[("selected", "white")],
    foreground=[("selected", "black")],
)  # <--- this function changes style selected row

style.configure(
    "Treeview.Column",
    rowheight=21,
    foreground="white",
    background="purple",
)  # <--- creates the basic table style

style.map(
    "Treeview.Column",
    background=[("selected", "white")],
    foreground=[("selected", "purple")],
)  # <--- this function changes style selected row

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

xscrollbar = Scrollbar(ws, orient=HORIZONTAL, troughcolor="green", command=treeview.xview)
yscrollbar = Scrollbar(ws, orient=VERTICAL, command=treeview.yview)
yscrollbar.config()
yscrollbar.pack(side=RIGHT, fill='y')
xscrollbar.pack(side=BOTTOM, fill='x')


# # plaatst de scrollbar
# ysb.grid(in_=_frame, row=0, column=1, sticky=NS, pady=10, padx=(0, 10))
# xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
# _frame.rowconfigure(0, weight=1)
# _frame.columnconfigure(0, weight=1)
# # attempt to color scrollbar

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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ws_lbl = Label(ws, text="Name", font=('calibri', 12, 'normal'), bg="black", fg="white")
ws_lbl.place(x=290, y=518)
ws_ent = Entry(ws, width=20, font=('Arial', 15, 'bold'), bg="black", fg="white")
ws_ent.place(x=220, y=540)
ws_btn1 = Button(ws, text='Search', width=8, font=('calibri', 12, 'normal'), command=search, bg="black", fg="white")
ws_btn1.place(x=480, y=540)
ws_btn2 = Button(ws, text='Reset', width=8, font=('calibri', 12, 'normal'), command=reset, bg="black", fg="white")
ws_btn2.place(x=600, y=540)

show_table()
ws.mainloop()
