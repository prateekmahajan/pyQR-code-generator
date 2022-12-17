from PIL import Image, ImageDraw, ImageFont
from pystrich.datamatrix import DataMatrixEncoder


def print_error(err):
    print(f"{type(err).__name__} was raised: {err}")
    pass


def generate_qr(text, all_fields):
    encoder = DataMatrixEncoder(text)
    encoder.save("QR.png")
    right_side_image(all_fields)
    pass


def right_side_image(text):
    sticker_name = f'sticker-{text[-1]}.png'
    size_of_font = 16
    try:
        font = ImageFont.truetype("./Arial.ttf", size_of_font, encoding="unic")
    except Exception as err:
        print_error(err)
    qr_img = Image.open('QR.png', 'r')

    # creating an outside white canvas (a box)
    qr_img_w, qr_img_h = qr_img.size
    sticker = Image.new('RGBA', (300, 150), (255, 255, 255, 255))
    bg_w, bg_h = sticker.size
    offset = (5, (bg_h - qr_img_h) // 2)
    sticker.paste(qr_img, offset)

    # Add text lines to the Canvas
    d = ImageDraw.Draw(sticker)
    sticker_h_offset = int((155 - (5 * len(text.split(':')[0]) / 2)) * 1)
    d.multiline_text((sticker_h_offset, 15), '\n'.join(text.split(':')), font=font, fill=(0, 0, 0))
    # need to use BOLD font family for Bold text

    sticker.save(sticker_name)
    pass
