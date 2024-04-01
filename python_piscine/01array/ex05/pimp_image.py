from PIL import Image

def ft_invert(pixels: list) -> list:
    inverted_pixels = [(abs(r - 255), abs(g - 255), abs(b - 255)) for r, g, b in pixels]
    return inverted_pixels



def ft_red(pixels: list) -> list:
    #code = *
    red_filter_pixels = [(r, 0, 0) for r, g, b in pixels]
    return red_filter_pixels


def ft_green(pixels: list) -> list:
    #code = -
    green_filter_pixels = [(0, g, 0) for r, g, b in pixels]
    return green_filter_pixels


def ft_blue(pixels: list) -> list:
    #code =
    blue_filter_pixels = [(0, 0, b) for r, g, b in pixels]
    return blue_filter_pixels


def ft_grey(pixels: list) -> list:
    #code = /
    grey_filter_pixels = [(max(r, g, b), max(r, g, b), max(r, g, b)) for r, g, b in pixels]
    return grey_filter_pixels
