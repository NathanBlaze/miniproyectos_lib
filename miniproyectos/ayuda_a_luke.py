from PIL import Image, ImageDraw, ImageFilter

imagen_original = Image.open("img/Luke.png")

vfx = Image.new("RGBA", imagen_original.size, (0, 0, 0, 0))

canvas = ImageDraw.Draw(vfx)

# Luke ha caído en el lado oscuro como su padre y ahora tiene un sable rojo xD
canvas.line([(380, 498), (-35, 34)], fill=(255, 0, 0), width=24)

for blurred in range(18):
    vfx = vfx.filter(ImageFilter.BLUR)

canvas = ImageDraw.Draw(vfx)

canvas.line([(380, 498), (-35, 34)], fill=(255, 255, 255), width=18)

vfx = vfx.filter(ImageFilter.BLUR)

imagen_original.alpha_composite(vfx)

imagen_original.save("img/Luke-vfx.png")
