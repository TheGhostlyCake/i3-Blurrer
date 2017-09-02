#!/bin/python

import os
from PIL import ImageFilter, Image, ImageDraw, ImageFont
from PIL import Image


os.system("scrot /tmp/tmp_screenshot.png")
img = Image.open("/tmp/tmp_screenshot.png")
img1 = img.filter(ImageFilter.GaussianBlur(radius=5))


draw = ImageDraw.Draw(img1,'RGBA')
font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 72)
font2= ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 36)
draw.rectangle([0,300,1920,430],(0,0,0,127),(0,0,0,127))
draw.text((0, 300),"Name",(255,255,255),font=font)
draw.text((0, 372),"Contact Informatoing",(255,255,255),font=font2)
img1.save("/tmp/tmp_screenshot1.png")
