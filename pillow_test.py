# pillow_test.py

from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from PIL import PSDraw

# saves an image in the directory in a variable
im = Image.open("Images/Grus-Plan.jpg")
im2 = Image.open("Images/Monkey-Puppet.jpg")
print(im.format, im.size, im.mode)

# saves a cropped image by the dimensions (left, upper, right, bottom)
# image pixels begin in upper left as (0,0)
box = (100, 100, 400, 400)
region = im.crop(box)

# processes a sub-rectangle and pasting it back
# this rotates the image 180 degrees and pastes it into image
region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)

# prints the region taken out and the image
# region.show()
# im.show()


'''
def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

merge(im, im2)

im.show()'''

# Geometrical transforms

# tuple gives new size
# out = im.resize((128, 128))
# out = im.rotate(45) # rotates degrees counterclockwise
# out = im.transpose(Image.Transpose.ROTATE_90) # can be used similarly to the rotate function

# resizing relative to a give size
'''
size = (100, 150)
with Image.open("Images/Monkey-Puppet.jpg") as im:
    ImageOps.contain(im, size).save("puppet_contain.png")
    ImageOps.cover(im, size).save("puppet_cover.png")
    ImageOps.fit(im, size).save("puppet_fit.png")
    ImageOps.pad(im, size, color="#f00").save("puppet_pad.png")

    # thumbnail can be used,
    # but will modify the image object in place
    im.thumbnail(size)
    im.save("puppet_thumbnail.png")
'''

# Color transformations, changing to L or RGB modes
'''
with Image.open("Images/Monkey-Puppet.jpg") as im:
    im = im.convert("L")
'''

# Image enhancement
# Filters
# out = im.filter(ImageFilter.DETAIL)

# Point operations (image contrast manipulation)
# out = im.point(lambda i: i * 1.2)
# can use point and paste methods together to selectively modify an image

# More image enhancement
'''
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
'''

# Contains basic support for image sequences (animation formats)
# use seek and tell methods to move frame by frame:
'''
with Image.open("animation") as im:
    im.seek(1)  # skip to second frame

    try:
        while 1:
            im.seek(im.tell() + 1)
            # do something to im here
    except EOFError:
        pass  # end of sequence
'''
# can also use the ImageSequence Iterator class to do this

# PostScript printing includes functions to print images, texts, and graphics

# example:
'''
with Image.open("hopper.ppm") as im:
    title = "hopper"
    box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)  # in points

    ps = PSDraw.PSDraw()  # default is sys.stdout or sys.stdout.buffer
    ps.begin_document(title)

    # draw the image (75 dpi)
    ps.image(box, im, 75)
    ps.rectangle(box)

    # draw title
    ps.setfont("HelveticaNarrow-Bold", 36)
    ps.text((3 * 72, 4 * 72), title)

    ps.end_document()
'''

# can use file-like object to read, seek, and tell
'''
with open("hopper.ppm", "rb") as fp:
    im = Image.open(fp)
'''

# can use BytesIO class to read from binary, can also use ContainerIO or TarIO to read from files
# can use urlopen to open url files
'''
from urllib.request import urlopen
url = "https://python-pillow.org/assets/images/pillow-logo.png"
img = Image.open(urlopen(url))
'''
