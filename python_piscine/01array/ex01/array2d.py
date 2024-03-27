def slice_me(family: list, start: int, end: int) -> list:
    try:
        print("My shape is : (" + str(len(family)) + ", " + str(len(family[0])) + ")")
        new_family = family[start:end]
        print("My new shape is : (" + str(len(new_family)) + ", " + str(len(new_family[0])) + ")")
        return new_family
    except TypeError:
        print("Argument error: wrong list type lmao")
        return -1
    except ValueError:
        print("Arguments error: list size")
        return -1

family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

print(slice_me(family, 0, 2))
print()
print(slice_me(family, 1, -2))