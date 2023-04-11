from tkinter import *
import qrcode as qr
from PIL import Image


def create():
    img = qr.make(value)
    fname = title + ".png"
    img.save(fname)
    print("Your "+title+" QRCode is successfully created !!!")
    print(value)

root = Tk()
root.title("QR Code Generator")
root.geometry("960x540")
root.resizable(0,0)
bg = PhotoImage(file="resources/bg.png")


label = Label(image=bg).pack()

a = Entry(root, width=24,justify=CENTER,bg=None).place(x=95,y=158)
b = Entry(root, width=24,justify=CENTER,bg=None,).place(x=95,y=243)

value = str(a)
title = str(b)
btn1 = Button(root, width=21,text = 'Generate QR',command=create).place(x=95,y=328)





root.mainloop()







