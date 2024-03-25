import qrcode as qr

link = input("Enter your URL ")
Name = input("Enter a name for QR Code ")
# filename = (f"{Name}.png")
filename1 = (f"c:\\c\\{Name}.png")

img = qr.make(link)
# img.save(filename)
img.save(filename1)
print(filename1)

# https://www.bajajfinservmarkets.in/