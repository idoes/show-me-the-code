"""create text on an image"""

from PIL import Image, ImageFont, ImageDraw

def what_text():
    return "hello Pillow"

def what_image():
    return "profile.png"

def what_font():
    return "Inconsolata-Regular.ttf"

def what_location(text_size_tuple, image_size_tuple, location_list):
    text_width, text_height = text_size_tuple
    image_width, image_height = image_size_tuple
    location_list.append(image_width - text_width)
    location_list.append(0)

def what_output():
    return "result.png"

def process():
    
    a_image = Image.open(what_image())
    a_draw = ImageDraw.Draw(a_image)
    a_text = what_text()
    a_font = ImageFont.truetype(what_font(), 15)
    # calculate the test location on the image
    location_list = list()
    what_location(a_font.getsize(a_text), a_image.size, location_list)

    #print str(text_width) + ", " + str(text_height)  # test
    #print str(image_width) + ", " + str(image_height)  # test

    a_draw.text((location_list[0], location_list[1]), a_text, fill="red", font=a_font)
    a_image.save(what_output(), "PNG")

process()