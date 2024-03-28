from PIL import Image
from zoom import zoom

def ft_load(path: str) -> list:
    image = Image.open(path)
    x_max, y_max = image.size
    pixels = []
    for x in range(x_max):
        for y in range(y_max):
            pixel = image.getpixel((x, y))
            pixels.append(pixel)
    print("The image format is: " + str(x_max) + "x" + str(y_max) + " " + str(image.format))
    zoom(path, 2)
    return pixels


# print(ft_load("/Users/theoke/Dev/python_piscine/01array/ex02/landscape.jpg"))
with open ("output.txt", "w") as file:
    file.write(str(ft_load("/Users/theoke/Dev/python_piscine/01array/images/landscape.jpg")))
with open ("output2.txt", "w") as file2:
    file2.write(str(ft_load("/Users/theoke/Dev/python_piscine/01array/images/animal.jpeg")))