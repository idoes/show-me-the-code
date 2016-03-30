import os, sys
from PIL import Image

small_image_size = (128, 128)

def process_command_arguments():
    for item in sys.argv[0:]:
        print "[command argument]: " + item

    return None

def os_module_exercise():
    for file_name in sys.argv[0:]:
        print "experience os.path module"
        print os.path.split(file_name)

def create_thumbnails():
    for in_file in sys.argv[1:]:
        thumbnail_name = os.path.splitext(in_file)[0] + ".thumbnail"
        if in_file != thumbnail_name:
            try:
                im = Image.open(in_file)
                im.thumbnail(small_image_size)
                im.save(thumbnail_name, "JPEG")
            except IOError:
                print"cannot create thumbnail for " + in_file



#process_command_arguments()
#os_module_exercise()
create_thumbnails()