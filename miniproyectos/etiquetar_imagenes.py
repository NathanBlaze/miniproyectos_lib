import os
import sys

from PIL import Image, ImageDraw

image_file = sys.argv[1]

image = Image.open(image_file)

width, height = image.size

draw = ImageDraw.Draw(image)

proportions = f"{width} x {height}"

text_width, text_height = draw.textsize(proportions)

x = 0
y = height - text_height

draw.text((x, y), proportions, fill=(255, 255, 255))

# Guardar la imagen con el nombre modificado
file_name, file_extension = os.path.splitext(image_file)
new_image_file = file_name + "-stamped" + file_extension
image.save(new_image_file)

print("Imagen guardada como:", new_image_file)
