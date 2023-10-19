import io
import qrcode

qr = qrcode.QRCode()
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #    Put website or text here

f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)

print(f.read())