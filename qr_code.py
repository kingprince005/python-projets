import qrcode

def generate_qr(data):
    # Create qr code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save it somewhere, change the extension as needed:
    img.save("qrcode.png")

generate_qr("https://instagram.com/king_prince_005?igshid=MzMyNGUyNmU2YQ==")