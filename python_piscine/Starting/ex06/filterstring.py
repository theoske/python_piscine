from ft_filter import ft_filter
from sys import argv


def argTest(argv) -> bool:
    if len(argv) != 3:
        return False

    str_to_test = argv[1]
    for c in str_to_test:
        if c.isalpha() is False and c != " ":
            return False

    try:
        int(argv[2])
    except ValueError:
        return False

    return True


def filterstring(string_to_filter: str):
    return True if len(string_to_filter) >= int(argv[2]) else False


def main(argv) -> int:
    if argTest(argv) is False:
        print(AssertionError.__name__ + ": Bad arguments.")
        return (1)
    list_string_to_filter = argv[1].split(" ")
    filtered = ft_filter(filterstring, list_string_to_filter)
    print(filtered)


if __name__ == "__main__":
    main(argv)
