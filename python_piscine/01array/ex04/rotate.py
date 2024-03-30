from PIL import Image
from os.path import basename

# crops the image inton a square.
# Since we get the pixels from column to column an than putdata
# puts them back in an image from row to row it automatically 
# makes the desired -90 degrees rotation for us.
def rotate(image: Image, path: str) -> Image:
    x_max, y_max = image.size
    side_length = min(x_max, y_max)
    x_start = (x_max - side_length) // 2
    y_start = (y_max - side_length) // 2
    squared_pixels = []
    for x in range(x_start, x_start + side_length):
        for y in range(y_start, y_start + side_length):
            pixel = image.getpixel((x, y))
            squared_pixels.append(pixel)
    squared_image = Image.new("RGB", (side_length, side_length))
    squared_image.putdata(squared_pixels)
    squared_image.save("rotated_" + basename(path))
    return squared_image
