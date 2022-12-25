import qrcode
img = qrcode.make('Some data here')
img.save("some_file.png")