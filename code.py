import qrcode as qr
from PIL import Image

value = input("Enter the link/text/number to generate QR Code: ")
title = input("Enter the file title to save: ")

img = qr.make(value)
fname = title + ".png"
img.save(fname)

print("Your "+title+" QRCode is successfully created !!!")

im = Image.open(fname)
im.show()