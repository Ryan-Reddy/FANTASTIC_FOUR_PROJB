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
#
#
# def show_table():
#     ws_ent.delete(0, END)
#     ws_ent.focus()
#     treeview.selection()
#     conn = None
#     try:
#         conn = connect(database_filepath)
#         curs = conn.cursor()
#         curs.execute("SELECT * FROM games_alltime")
#
#         fetchdata = treeview.get_children()
#         for elements in fetchdata:
#             treeview.delete(elements)
#
#         data = curs.fetchall()
#         for d in data:
#             treeview.insert("", END, values=d,
#         tags="body",)
#
#         conn.commit()
#     except Exception as e:
#         showerror("Fail", e)
#         conn.rollback()
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# def search():
#     treeview.selection()
#     fetchdata = treeview.get_children()
#     for f in fetchdata:
#         treeview.delete(f)
#     conn = None
#     try:
#         conn = connect(database_filepath)
#         core = conn.cursor()
#         db = "select * from games_alltime where name or developer LIKE '%s%s%s' "; #<--- searches for arguments mentioned below
#         name = ws_ent.get()
#         if (len(name) < 2) or (not name.isalpha()):
#             showerror("fail", "invalid name")
#         else:
#             arguments = ('%', name, '%',)  #<--- infill of arguments, uses search infill + double wildcard
#             core.execute(db % (arguments))
#             print(db % (arguments))
#             data = core.fetchall()
#             for d in data:
#                 treeview.insert("", END, values=d)
#
#     except Exception as e:
#         showerror("issue", e)
#
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# def sort_by():
#     treeview.selection()
#     fetchdata = treeview.get_children()
#     for f in fetchdata:
#         treeview.delete(f)
#     conn = None
#     try:
#         conn = connect(database_filepath)
#         core = conn.cursor()
#         db = "select * from games_alltime where name or developer = '%s' "
#         name = ws_ent.get()
#         if (len(name) < 2) or (not name.isalpha()):
#             showerror("fail", "invalid name")
#         else:
#             core.execute(db % (name))
#             data = core.fetchall()
#             for d in data:
#                 treeview.insert("", END, values=d)
#
#     except Exception as e:
#         showerror("issue", e)
#
#     finally:
#         if conn is not None:
#             conn.close()
#
# def reset():
#     show_table()
#
# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#
# treeview = ttk.Treeview(ws, columns=("#1", "#2", "#3", "#4", "#5"), show='headings', height=21)  #<--- maakt treeview headings
# treeview.pack()
#
# treeview.heading("#1", text="Appid", command=lambda c="#1": sort_by(treeview, c, 0))
# treeview.column("#1", minwidth=10, width=50, stretch=0)
# treeview.heading("#2", text="Name", command=lambda c="#2": sort_by(treeview, c, 0))
# treeview.column("#2", minwidth=10, width=220, stretch=0)
# treeview.heading("#3", text="Developer", command=lambda c="#3": sort_by(treeview, c, 0))
# treeview.column("#3", minwidth=10, width=120, stretch=0)
# treeview.heading("#4", text="Positive Ratings", command=lambda c="#4": sort_by(treeview, c, 0))
# treeview.column("#4", stretch=YES, width=60)
# treeview.heading("#5", text="Negative Ratings", command=lambda c="#5": sort_by(treeview, c, 0))
# treeview.column("#5", stretch=YES, width=50)
# treeview.tag_configure("body", background="black", foreground='green')  #<--- colors table body
#
#
#
#
# style = ttk.Style()
# style.theme_use("default")
# style.map("Treeview")
# style.configure(
#     "Treeview.Heading",
#     rowheight=21,
#     foreground= "white",
#     background="black",
# )  # <--- creates the heading style
# #
# # style.map(
# #     "Treeview.Heading",
# #     background=[("selected", "purple")],
# #     foreground=[("selected", "black")],
# # )  # <--- this function changes style selected row
#
# # Geeft aan waar de tabel in het grid moet
# # treeview.grid(in_=_frame, row=0, column=0, sticky=NSEW)
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # sorteert columns naar klik op de headers TODO implementeer slimmere algoritmes dmv SQL updates, see search
# """"
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/treeview.html
#
# Setting a custom sort function
# It is also possible to set a custom comparison function in order to change the sorting behaviour.
# As an example we will create a comparison function that sorts case-sensitive.
# In the example above the sorted list looked like:
#
# alfred
# Alfred
# benjamin
# Benjamin
# charles
# Charles
# david
# David
# The case-sensitive sorted list will look like:
#
# Alfred
# Benjamin
# Charles
# David
# alfred
# benjamin
# charles
# david
#
# First of all a comparison function is needed. This function gets two rows and has to return a negative integer
# if the first one should come before the second one,
# zero if they are equal and a positive integer if the second one should come before the first one.
#
# def compare(model, row1, row2, user_data):
#     sort_column, _ = model.get_sort_column_id()
#     value1 = model.get_value(row1, sort_column)
#     value2 = model.get_value(row2, sort_column)
#     if value1 < value2:
#         return -1
#     elif value1 == value2:
#         return 0
#     else:
#         return 1
# Then the sort function has to be set by Gtk.TreeSortable.set_sort_func().
#
# model.set_sort_func(0, compare, None)"""
#
#
# def sort_by(tree, col, descending):
#     # grab values to sort
#     header_data = [(tree.set(child, col), child) for child in tree.get_children("")]
#     print(header_data)
#
#     # TODO if the data to be sorted is numeric change to float
#     # data =  change_numeric(data)
#
#     for ix, item in enumerate(header_data):
#         tree.move(item[1], "", ix)  #<---    # sort the data in place
#         # print(f'ix  {ix}    ---    item[1]{item[1]}')
#     header_data.sort(reverse=descending)    # switch the heading, so it will sort in the opposite direction.
#
#     tree.heading(
#         col, command=lambda local_col=col: sort_by(tree, local_col, int(not descending))
#     )
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# xscrollbar = Scrollbar(ws, orient=HORIZONTAL, troughcolor="green", command=treeview.xview)
# yscrollbar = Scrollbar(ws, orient=VERTICAL, command=treeview.yview)
# yscrollbar.config()
# yscrollbar.pack(side=RIGHT, fill='y')
# xscrollbar.pack(side=BOTTOM, fill='x')
#
#
# # # plaatst de scrollbar
# # ysb.grid(in_=_frame, row=0, column=1, sticky=NS, pady=10, padx=(0, 10))
# # xsb.grid(in_=_frame, row=1, column=0, sticky=EW)
# # _frame.rowconfigure(0, weight=1)
# # _frame.columnconfigure(0, weight=1)
# # # attempt to color scrollbar
#
# style.configure(
#     "Vertical.TScrollbar",
#     background="black",
#     bordercolor="black",
#     troughcolor="black",
#     highlightcolor="white",
# )
# style.configure(
#     "Horizontal.TScrollbar",
#     background="black",
#     bordercolor="black",
#     troughcolor="black",
#     highlightcolor="purple",
# )
#
#
# def cur_treeview(a):
#
#     curItem = treeview.focus()
#     info_string = treeview.item(curItem)
#     print(f"info_string = treeview.item(curItem) = {info_string}")
#     print(curItem)
#     print(treeview.index(curItem))
#     # rowID = treeview.identify('item', event.x, event.y)
#     # print(rowID)
#     # print(f'indetify row: {rowID}')  #<---TODO: implement Returns the item ID of the item at position y.
#
#     treeview.rowconfigure(treeview.index(curItem), minsize=15)
#
#     # show selected info in buttons:
#     total_info = info_string.get("values")
#     positive_ratings = total_info[4]  # <--- assign
#     negative_ratings = total_info[5]  # <--- assign
#
#     print(f"sel onscr. in table : total_info = {total_info}")
#
#     mainscreen.sel_item_label.config(text=total_info[0], anchor=E)
#     print(f"title = {total_info[0]}")
#
#     print(f"positive ratings = {positive_ratings}")
#     mainscreen.selectPosRat_label.config(text=positive_ratings)
#
#     print(f"negative ratings = {negative_ratings}")
#
#     mainscreen.selectNegRat_label.config(text=negative_ratings)
#     symbol = "%"
#     ratingsperc = f"{ratings_calc(total_info[5], total_info[4])}{symbol}"
#     mainscreen.configurable_label.config(text=ratingsperc)  # <--- percentagecalc in action
#     mainscreen.selectgamescore_label.config(text=ratingsperc, bg="green")
#
#     ratings_calc(negative_ratings, negative_ratings)
#     return total_info
#
# treeview.bind("<ButtonRelease-1>", cur_treeview)  # <--- grab data from clicked row


# *************************************************************************************************
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
database_filepath = "steam_database.db"


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
