from ft_filter import ft_filter
from sys import argv


def argTest(argv) -> bool:
    if len(argv) != 3:
        return False

    str_to_test = argv[1]

    try:
        int(argv[2])
    except ValueError:
        return False

    return all([False if c.isalpha() is False and c != " " else True for c in str_to_test]) is True

def main(argv) -> int:
    if argTest(argv) is False:
        print(AssertionError.__name__ + ": Bad arguments.")
        return 1
    list_string_to_filter = argv[1].split(" ")
    filtered = ft_filter(lambda string_to_filter: len(string_to_filter) >= int(argv[2]), list_string_to_filter)
    print(filtered)
    return 0


if __name__ == "__main__":
    main(argv)
