from sys import argv


def caseCounter(a: str) -> str:
    char_count = len(a)
    up_count = 0
    low_count = 0
    digit_count = 0
    punctuation_count = 0
    space_count = 0
    punctuation_chars = {"!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", ",", "{", "|", "}", "~"}
    for i in a:
        if i.isupper():
            up_count+=1
        elif i.islower():
            low_count+=1
        elif i.isdigit():
            digit_count+=1
        elif i in punctuation_chars:
            punctuation_count+=1
        elif i.isspace():
            space_count+=1
    res = "\nThe text contains " + str(char_count) + " characters:\n" + str(up_count) + " upper letters\n" + str(low_count) + " lower letters\n" + str(punctuation_count) + " punctuation marks\n" + str(space_count) + " spaces\n" + str(digit_count) + " digits\n"
    return res


def main(argv) -> int:
    """plays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces."""
    if len(argv) > 2:
        print(AssertionError.__name__)
        return 1
    a = "" if len(argv) == 1 else argv[1]
    if a == "" or a is None:
        try:
            a = input("Write the string you want to count:\n")
        except:
            return 1
    else:
        a = argv[1]
    print(caseCounter(a))
    return 0


if __name__ == "__main__":
    main(argv)
