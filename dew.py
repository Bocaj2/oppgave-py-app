from PIL import Image, ImageOps

img1 = Image.open("frosk.png")
img2 = ImageOps.fit(img1, (760,760))
ramme = Image.open("bilde.png")
polar = ramme.convert("RGB")
polar.paste(img2,(64,64))
polar.show()