# How to Create a QR Code Using Python and qrcode

This guide explains how to generate a QR code using Python and the `qrcode` library.

## Prerequisites

Make sure you have Python installed. You can download Python from [python.org](https://www.python.org/downloads/).

## Step 1: Install the `qrcode` library

Open your terminal or command prompt and run the following command to install the library:

```bash
pip install qrcode[pil]
```

## Step 2: Write a Python script to create the QR code

Create a new Python file named `generate_qr.py` and add the following code:

```python
import qrcode

# Data to be encoded in the QR code
data = "https://www.example.com"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # QR code size (1-40, 1 being smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in pixels
    border=4,  # Border thickness in boxes
)

# Add data to the QRCode object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
```

## Step 3: Run the script

Run your Python script from the terminal or command prompt:

```bash
python generate_qr.py
```

After running the script, you will see a file named `qrcode.png` in your current directory.

## Step 4: View your QR code

Open the `qrcode.png` file with an image viewer or web browser to see your generated QR code.

## Customizing your QR code

You can customize your QR code by modifying the parameters:

- `data`: change this to the text or URL you want to encode.
- `version`: adjust this to make the QR code bigger or smaller.
- `box_size`: change this to modify the pixel size of each QR code box.
- `border`: adjust the border thickness.
- `fill_color` and `back_color`: modify these to change the colors of the QR code.

## References

- [qrcode Documentation](https://pypi.org/project/qrcode/)

---

Enjoy creating your QR codes!
