import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

qr.make(fit=True)

img = qr.make_image(back_color="black", fill_color="white")

img.save("example_python_QR_file_inverted.png")