def main():
    while True:
        user_input = input("Fraction: ")
        fraction_to_perc = convert(user_input)
        if fraction_to_perc is not None:
            perc = gauge(fraction_to_perc)
            if perc is not None:
                print(perc)
                break


def convert(fraction):
    try:
        x, y = fraction.strip().split("/")
        return int(int(x) / int(y) * 100)
    except ValueError:  # Given fraction contains type non-integer.
        raise ValueError
    except ZeroDivisionError:  # Cannot divide by 0.
        raise ZeroDivisionError


def gauge(percentage):
    int(percentage)
    if 100 >= percentage >= 99:
        return "F"
    elif 1 >= percentage >= 0:
        return "E"
    elif percentage > 100:
        return None
    elif percentage < 0:
        return None
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()