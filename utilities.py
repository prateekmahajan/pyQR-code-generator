import pyqrcode
import png
from PIL import Image, ImageDraw, ImageFont

def print_error(err):
    print(f"{type(err).__name__} was raised: {err}")
    pass
def generate_qr(text):
    url = pyqrcode.create(text)
    url.png("QR.png", scale=3)
    right_side_image('text1lajsdklajsdkljasljd', 'text2')
    pass
def right_side_image(text1, text2):
    sticker_name = 'sticker.png'
    try:
        font = ImageFont.truetype("./Arial.ttf", 10, encoding="unic")
    except Exception as err:
        print_error(err)
    qr_img = Image.open('QR.png', 'r')
    # creating an outside white canvas (a box)
    qr_img_w, qr_img_h = qr_img.size
    sticker = Image.new('RGBA', (200, 100), (255, 255, 255, 255))
    bg_w, bg_h = sticker.size
    offset = ((bg_h - qr_img_h) // 2, (bg_h - qr_img_h) // 2)
    sticker.paste(qr_img, offset)
    # Add text lines to the Canvas
    d = ImageDraw.Draw(sticker)
    sticker_h_offset = int((155 - (5 * len(text1) / 2))*1)
    # d.text((sticker_h_offset, 22), text1, font=font, fill=(0, 0, 0))
    # seq_h_offset = int(155 - (5 * len(text2) / 2))
    # d.text((seq_h_offset, 37), text2, font=font, fill=(0, 0, 0))
    d.multiline_text((sticker_h_offset, 0), "0101DW5009line1\n0101DW5009line2\n0101DW5009line3\n0101DW5009line4\n0101DW5009line5\n0101DW5009line6\n0101DW5009line7", font=font, fill=(0, 0, 0))
    # need to use BOLD font family for Bold text
    sticker.save(sticker_name)
    pass

# generate_qr("oh_la la la")
