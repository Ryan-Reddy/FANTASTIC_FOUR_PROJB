from tkinter import *
from PIL import Image, ImageTk


window = Tk()

image = r"C:\Users\RyRy\PycharmProjects\FANTASTIC_FOUR_PROJB\steamlogolarge.jpg"

img = Image.open(image)
ph = ImageTk.PhotoImage(img)
img.show()


import sys
print(sys.executable)

Label(window, image=ph).pack()
window.mainloop()
#
# def change_label_old():
#     # decides when to end the recursive iteration
#     for i in lst[:-1]:
#         print(i)
#         Slabel.configure(text=i)
#         update_idletasks()
#         time.sleep(random.uniform(.5, .8))
#
#     #     img = Image.open(i)
#     #     ph = ImageTk.PhotoImage(img)
#     #     img_label.configure(image=ph)
#     #     time.sleep(random.uniform(.5, .8))
