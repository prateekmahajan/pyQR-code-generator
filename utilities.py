from PIL import Image, ImageDraw, ImageFont
from pystrich.datamatrix import DataMatrixEncoder
import os

def print_error(err):
    print(f"{type(err).__name__} was raised: {err}")
    pass


def generate_qr(text, all_fields):
    encoder = DataMatrixEncoder(text)
    encoder.save("temp.png")
    right_side_image(all_fields)
    pass


def right_side_image(all_fields):
    sticker_name = 'sticker-{}.png'.format(all_fields.split(':')[-1])
    size_of_font = 16
    try:
        font = ImageFont.truetype("./Arial.ttf", size_of_font, encoding="unic")
    except Exception as err:
        print_error(err)
    qr_img = Image.open('temp.png', 'r')

    # creating an outside white canvas (a box)
    qr_img_w, qr_img_h = qr_img.size
    sticker = Image.new('RGBA', (300, 150), (255, 255, 255, 255))
    bg_w, bg_h = sticker.size
    offset = (5, (bg_h - qr_img_h) // 2)
    sticker.paste(qr_img, offset)

    # Add all_fields lines to the Canvas
    d = ImageDraw.Draw(sticker)
    sticker_h_offset = int((155 - (5 * len(all_fields.split(':')[0]) / 2)) * 1)
    d.multiline_text((sticker_h_offset, 15), '\n'.join(all_fields.split(':')), font=font, fill=(0, 0, 0))
    # need to use BOLD font family for Bold text

    # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    sticker.save(r"E:\Desktop\genQRs\\"+sticker_name)
    pass
