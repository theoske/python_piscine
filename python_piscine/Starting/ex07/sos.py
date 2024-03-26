from sys import argv
from unicodedata import unicodedata


def argTester(argv) -> bool:
    return len(argv) == 2 and all([True if c.isalnum() or c == " " else False for c in argv[1]])


def strip_accents(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn')


def morseTranslation(string_to_translate: str) -> str:
    string_to_translate = strip_accents(string_to_translate.upper())
    MORSE_DICT = {" ": "/ ", 'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
    'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
    'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
    'Y': '-.-- ', 'Z': '--.. ', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'}
    return ''.join([MORSE_DICT[char_to_translate] for char_to_translate in string_to_translate])



def main(argv) -> int:
    if argTester(argv) is False:
        print(AssertionError.__name__ + ": Argument error.")
        return 1
    print(morseTranslation(argv[1]))
    return 0


if __name__ == "__main__":
    main(argv)
