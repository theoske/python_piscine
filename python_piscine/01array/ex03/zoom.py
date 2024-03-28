from PIL import Image
from os.path import basename


def zoom(path : str, zoom: float):
    image = Image.open(path)
    width, height = image.size
    zoomed_w = width // zoom
    zoomed_h = height // zoom
    middle_w = width // 2
    middle_h = height // 2
    zoomed_image = image.crop((middle_w - (zoomed_w / 2), middle_h - (zoomed_h / 2), middle_w + (zoomed_w / 2), middle_h + (zoomed_h / 2)))
    zoomed_image.save("zoomed_" + basename(path))
    print("The croped image format is: " + str(zoomed_w) + "x" + str(zoomed_h) + " " + str(zoomed_image.format))
    



