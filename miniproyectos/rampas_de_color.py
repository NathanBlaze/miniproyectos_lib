from PIL import Image

width = 256
height = 256
rgb_image = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        r = x
        g = y
        b = (x + y) // 2
        rgb_image.putpixel((x, y), (r, g, b))

rgb_image.show()
