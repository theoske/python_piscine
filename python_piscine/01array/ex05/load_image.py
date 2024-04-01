from pimp_image import *
from PIL import Image
from os.path import basename

def ft_load(path: str) -> list:
    image = Image.open(path)
    x_max, y_max = image.size
    pixels = []
    for y in range(y_max):
        for x in range(x_max):
            pixel = image.getpixel((x, y))
            pixels.append(pixel)
    print("The image format is: " + str(x_max) + "x" + str(y_max) + " " + str(image.format))
    # filtered_image = ft_invert(pixels)
    # filtered_image = ft_blue(pixels)
    # filtered_image = ft_green(pixels)
    filtered_image = ft_grey(pixels)
    # filtered_image = ft_red(pixels)
    squared_image = Image.new("RGB", (x_max, y_max))
    squared_image.putdata(filtered_image)
    squared_image.save("filtered_" + basename(path))
    return pixels


# print(ft_load("/Users/theoke/Dev/python_piscine/01array/ex02/landscape.jpg"))
with open ("output.txt", "w") as file:
    file.write(str(ft_load("/Users/theoke/Dev/python_piscine/01array/images/landscape.jpg")))
with open ("output2.txt", "w") as file2:
    file2.write(str(ft_load("/Users/theoke/Dev/python_piscine/01array/images/animal.jpeg")))
