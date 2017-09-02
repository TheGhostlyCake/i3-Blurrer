from mss import mss
from PIL import ImageFilter, ImageDraw, ImageFont, Image
from argparse import ArgumentParser

def main(title, subtitle, outfile, radius):
    with mss() as sct:
        # grab screenshot from monitor 0
        sct_img = sct.grab(sct.monitors[0])
    im = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
    
    img1 = im.filter(ImageFilter.GaussianBlur(radius=radius))
    
    draw = ImageDraw.Draw(img1, 'RGB')
    font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 72)
    font2 = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 36)
    draw.rectangle([0, 300, 1920, 430], (0, 0, 0, 127), (0, 0, 0, 127))
    draw.text((0, 300), title, (255, 255, 255), font=font)
    draw.text((0, 372), subtitle, (255, 255, 255), font=font2)
    img1.save(outfile)


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate an overlaid blurred image of desktop with text on it')
    parser.add_argument('title', help='title text')
    parser.add_argument('subtitle', help='subtitle text')
    parser.add_argument('outfile', help='name of the output file')
    parser.add_argument('--radius', type=int, help='gaussian blur radius', default=5)
    args = parser.parse_args()
    main(args.title, args.subtitle, args.outfile, args.radius)
