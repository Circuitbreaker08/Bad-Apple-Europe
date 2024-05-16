from PIL import Image

im = Image.open("europe_source.png").convert("RGB").resize((480, 360))

provinces: list[set] = []
borders = []
ocean = []
water = (112, 145, 196)
taken_pixels = set()

for x in range(im.size[0]):
    for y in range(im.size[1]):
        color = im.getpixel((x, y))
        if (x, y) in taken_pixels:
            continue
        elif (
            color[0] <= 190 and
            color[1] <= 190 and
            color[2] <= 190
        ):
            borders.append((x, y))
            taken_pixels.add((x, y))
        elif (
            color[0] >= water[0] - 5 and color[0] <= water[0] + 5 and
            color[1] >= water[1] - 5 and color[1] <= water[1] + 5 and
            color[2] >= water[2] - 5 and color[2] <= water[2] + 5
        ):
            ocean.append((x, y))
            taken_pixels.add((x, y))
        else:
            merge_provinces = []
            for province in provinces:
                if (x + 1, y) in province or (x - 1, y) in province or (x, y + 1) in province or (x, y - 1) in province:
                    merge_provinces.append(province)
            if merge_provinces == []:
                provinces.append(set(((x, y),)))
            else:
                new_province = set()
                for province in merge_provinces:
                    provinces.pop(provinces.index(province))
                    new_province |= province
                provinces.append(new_province)
            taken_pixels.add((x, y))

print(borders)
print(ocean)
print(provinces)