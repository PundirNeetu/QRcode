#pip install qrcode[pil]
import qrcode

# LinkedIn profile URL
linkedin_url = "https://www.linkedin.com/in/neetu-pundir/"

# Create QR Code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box
    border=4,  # thickness of the border
)

qr.add_data(linkedin_url)  # Add LinkedIn URL data to the QR code
qr.make(fit=True)  # Generate the QR code

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("linkedin_qr_code.png")
print("QR code generated and saved as linkedin_qr_code.png")
