import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=dQw4w9WgXcQ') #    Put website or text here

img.save("example_python_QR_file.png")