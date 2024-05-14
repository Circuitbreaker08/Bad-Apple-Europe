from PIL import Image

im = Image.open("europe_source.png").convert("RGB")

provinces = []
taken_pixels = set()

for x in im.size[0]:
    for y in im.size[1]:
        if (x, y) in taken_pixels:
            continue
        

        """
        take each pixel
        propogate claim
        """