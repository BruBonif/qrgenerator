#ONLY WORKS ON VSCODE




#imports the library qrcode
import qrcode

#data in the qr code
data = "Hello world"

#custom the size qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#adds the data at the qrcode
qr.add_data(data)

#creates the qrcode
qr.make(fit=True)

#puts the qrcode in a variable and custom colors
img = qr.make_image(fill_color = 'black', back_color = 'white')

#saves the image in the pc
img.save('D:/Boni/myqr.png')