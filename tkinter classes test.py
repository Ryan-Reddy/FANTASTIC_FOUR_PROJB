"""this is a basic class intance I wrote to remember how to create and use a class instance,
for Object oriented programming
DO not delete"""
from tkinter import *

root = Tk()


class Style_Class:
    def __init__(self, back_color, font_color, font_title, font_main, pack):
        self.back_color = back_color
        self.font_color = font_color
        self.font_title = font_title
        self.font_main = font_main
        self.pack = pack


Font_Class = Style_Class(
    "black",
    "white",
    'FF Din OT", 14, "bold',
    (
        "Arial" or "Helvetica",
        12,
    ),
)

Label(text="hello", bg=my_style_class.back_color, fg=my_style_class.font_color).pack(
    pady=20, padx=300
)
Label(text="my", bg=my_style_class.back_color, fg=my_style_class.font_color).pack(
    pady=20, padx=300
)
Label(text="name", bg=my_style_class.back_color, fg=my_style_class.font_color).pack(
    pady=20, padx=300
)
Label(text="is", bg=my_style_class.back_color, fg=my_style_class.font_color).pack(
    pady=20, padx=300
)

root.mainloop()
