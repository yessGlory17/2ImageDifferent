from src.lib.Resim import Resim
from src.lib.Dedektor import Dedektor
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

root = Tk()

root.geometry("1980x1080")

root.title("OpenCV ile İki Resim Arasındaki Farkı Bulma")

i = Image.open("default.png")
i = i.resize((450, 310), Image.ANTIALIAS)
i = ImageTk.PhotoImage(i)


lbl = Label(root, height=350, width=500)
default = Image.open("default.png")
default = ImageTk.PhotoImage(default)
lbl.config(image=default)
lbl.image = default
lbl.grid(row=0, column=0)

lbl2 = Label(root, height=350, width=500)
default = Image.open("default.png")
default = ImageTk.PhotoImage(default)
lbl2.config(image=default)
lbl2.image = default
lbl2.grid(row=0, column=4)

lbl3 = Label(root, height=350, width=500)
lbl3.config(image=default)
lbl3.image = default
lbl3.grid(row=3, column=2)


def dosyaAc():
    path = askopenfilename(filetypes=(
        ("JPG Files", "*.jpg *.jpeg"), ("PNG Files", "*.png")))


def resim1Sec():
    path = askopenfilename(filetypes=(
        ("All Image Files", "*.jpg *.jpeg *.png"), ("JPG Files", "*.jpg *.jpeg"), ("PNG Files", "*.png")))
    j = Image.open(path)
    j = ImageTk.PhotoImage(j)
    lbl.config(image=j)
    lbl.image = j
    global i1
    i1 = path
    print(i1)


B1 = Button(root, text="Choose Image 1", command=resim1Sec)
B1.grid(row=1, column=0)


def resim2Sec():
    path = askopenfilename(filetypes=(
        ("All Image Files", "*.jpg *.jpeg *.png"), ("JPG Files", "*.jpg *.jpeg"), ("PNG Files", "*.png")))
    #path = askopenfilename(filetypes=(("JPG Files","*.jpg *.jpeg"),("PNG Files","*.png")))
    j = Image.open(path)
    j = ImageTk.PhotoImage(j)
    lbl2.config(image=j)
    lbl2.image = j
    global i2
    i2 = path
    print(i2)


B2 = Button(root, text="Choose Image 1", command=resim2Sec)
B2.grid(row=1, column=4)


def calistir():
    #path = askopenfilename(filetypes=(("JPG Files","*.jpg, *.jpeg"),("PNG Files","*.png")))
    a1 = Resim(i1)
    a2 = Resim(i2)
    Dedektor.olcekle(a1, a2)
    path = Dedektor.fark(a1, a2)
    print(path.src)
    j = Image.open(path.src)
    j = ImageTk.PhotoImage(j)
    lbl3.config(image=j)
    lbl3.image = j
    print("farkı bulma çalıştı")


B3 = Button(root, text="Find!", command=calistir)
B3.grid(row=6, column=2)

root.mainloop()
