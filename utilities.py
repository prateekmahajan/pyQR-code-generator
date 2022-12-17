import pyqrcode
import png
from pyqrcode import QRCode

def generate_qr(text):
    url = pyqrcode.create(text)
    url.png("myqr.png", scale=6)
    pass

