
# use the pillow fork of PIL: https://pillow.readthedocs.io/en/latest/installation.html
from PIL import Image

# load the head image into the program
head = Image.open("head 1.png")
# load the ears image into the program
ears = Image.open("ears 1.png")
# load the eyes image into the program
eyes = Image.open("eyes 1.png")
# load the background image into the program
background = Image.open("background.png")
# question: does it matter what order we load the images in?

# start making the final alien picture. here we add the background
alien = background.copy()
# add the head to the final alien picture
alien.paste(head, (0,0), head)
# add the ears to the final alien picture
alien.paste(ears, (0,0), ears)
# add the eyes to the final alien picture
alien.paste(eyes, (0,0), eyes)
# question: does it matter in what order we add the images to the final alien picture?

# show the alien in the computer's default image viewer.
alien.show()