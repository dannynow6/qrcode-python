import qrcode
import qrcode.constants 

# define data 
data = "https://www.codenoobs.io"

# create a QR code object 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code 
qr.add_data(data) 
qr.make(fit=True) 

# Create an image from the QR code instance 
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image 
img.save("codenoobs_qr.png") 



