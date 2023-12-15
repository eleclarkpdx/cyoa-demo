
# use the pillow fork of PIL: https://pillow.readthedocs.io/en/latest/installation.html
from PIL import Image

head = Image.open("head 1.png")
ears = Image.open("ears 1.png")
eyes = Image.open("eyes 1.png")
background = Image.open("background.png")

alien = background.copy()
alien.paste(head, (0,0), head)
alien.paste(ears, (0,0), ears)
alien.paste(eyes, (0,0), eyes)

alien.show()