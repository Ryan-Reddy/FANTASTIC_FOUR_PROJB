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

