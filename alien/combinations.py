
# use the pillow fork of PIL: https://pillow.readthedocs.io/en/latest/installation.html
from PIL import Image

for head in range(1,8):
    for ear in range(1,8):
        for eye in range(1,8):
            alien = Image.open("background.png")
            headImg = Image.open("head %s.png"%(head))
            earsImg = Image.open("ears %s.png"%(ear))
            eyesImg = Image.open("eyes %s.png"%(eye))
            alien.paste(headImg, (0,0), headImg)
            alien.paste(earsImg, (0,0), earsImg)
            alien.paste(eyesImg, (0,0), eyesImg)
            alien.save("combinations/%s%s%s.png"%(head, ear, eye), format="png")