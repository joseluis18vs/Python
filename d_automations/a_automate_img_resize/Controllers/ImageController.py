from PIL import Image
from datetime import datetime

'''
Method gray_scale, convert color img to gray scale.
'''


def gray_scale(path, size):
    img = Image.open(path)
    return img.convert(size)


'''
Method resize_img, generate image copy new size.
'''


def resize_img(path):
    config = input("Configuración: ")
    size = size_chooser(config)
    img = Image.open(path)
    return img.resize((size[0], size[1]))


def resize_batch(path):
    config = input("Configuración: ")
    size = size_chooser(config)

    # TO DO:
    # Select image file from list
    # Resize and save images.


def save_image(img_object):
    now = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
    img_object.save(f"image_resized{now}.png")


def size_chooser(config):
    if config == "ac":
        return [300, 300]  # H | W
    elif config == "ah":
        return [450, 300]  # H | W
    elif config == "bc":
        return [400, 400]  # H | W
    elif config == "bh":
        return [550, 400]  # H | W
    elif config == "cc":
        return [500, 500]  # H | W
    elif config == "ch":
        return [650, 500]  # H | W
