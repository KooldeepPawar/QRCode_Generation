import qrcode as qr

link = input("Enter your URL ")
Name = input("Enter a name for QR Code ")
filename = (f"{Name}.png")

img = qr.make(link)
img.save(filename)
