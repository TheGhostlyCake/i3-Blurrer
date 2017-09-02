from mss import mss
from PIL import ImageFilter, ImageDraw, ImageFont, Image
import argparse

def main():
    with mss() as sct:
        # grab screenshot from monitor 0
        sct_img = sct.grab(sct.monitors[0])
    im = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
    
    img1 = im.filter(ImageFilter.GaussianBlur(radius=5))
    
    draw = ImageDraw.Draw(img1, 'RGB')
    font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 72)
    font2 = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 36)
    draw.rectangle([0, 300, 1920, 430], (0, 0, 0, 127), (0, 0, 0, 127))
    draw.text((0, 300), "Name", (255, 255, 255), font=font)
    draw.text((0, 372), "Contact Information", (255, 255, 255), font=font2)
    img1.save("/tmp/tmp_screenshot1.png")


if __name__ == "__main__":
    main()
