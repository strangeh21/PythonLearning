
def main():
    while True:
        user_input = input("Fraction: ").strip()
        fuel_level = fuelGauge(user_input)
        if fuel_level != None:
            print(fuel_level)
            break


def fuelGauge(input):
    try:
        a, b = input.split("/")
        int(a)
        int(b)
        perc_value = (float(a) / float(b)) * 100
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    else:
        match perc_value:
            case perc_value if 100 >= perc_value >= 99:
                perc_value = "F"
            case perc_value if 1 >= perc_value >= 0:
                perc_value = "E"
            case perc_value if perc_value > 100:
                perc_value = None
            case _:
                perc_value = f"{perc_value:.0f}%"
        return perc_value


if __name__ == "__main__":
    main()