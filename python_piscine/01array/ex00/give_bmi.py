def give_bmi(height_list: list[int | float], weight_list: list[int | float]) -> list:
    try:
        bmi_list = [weight / (height**2) for height, weight in zip(height_list, weight_list)]
        return bmi_list
    except TypeError:
        print("Arguments error: wrong list type.")
        return -1
    except ValueError:
        print("Arguments error: height_list and weight_list are not the same length")
        return -1



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        is_below_limit = [True if bmi_value > limit else False for bmi_value in bmi]
        return is_below_limit
    except TypeError:
        print("Arguments error: wrong bmi list type.")
        return -1


def main():
    """tests from the exercise subject"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    print(type(height))
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    return 0


if __name__ == "__main__":
    main()
