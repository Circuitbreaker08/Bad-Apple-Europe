from PIL import Image

im = Image.open("europe_source.png").convert("RGB").resize((480, 360))
water = (112, 145, 196)

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixel = im.getpixel((x, y))
        if (
            pixel[0] <= 190 and
            pixel[1] <= 190 and
            pixel[2] <= 190
        ):
            color = (127, 127, 127)
        elif (pixel[0] >= water[0] - 5 and pixel[0] <= water[0] + 5 and
            pixel[1] >= water[1] - 5 and pixel[1] <= water[1] + 5 and
            pixel[2] >= water[2] - 5 and pixel[2] <= water[2] + 5):
            color = (0, 0, 0)
        else:
            color = (200, 200, 200)
        im.putpixel((x, y), color)

im.show()