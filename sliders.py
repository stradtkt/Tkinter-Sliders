from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gowebkit.com Image Viewer")
root.iconbitmap("c:/gui/image.png")
root.geometry("700x600")

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + vertical.get())

vertical = Scale(root, from_=0, to=200)
vertical.pack()
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()
my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()