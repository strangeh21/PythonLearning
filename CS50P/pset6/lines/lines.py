import sys


def main():
    py_file = check_arguments(sys.argv)
    print(count_lines(py_file))


def check_arguments(arguments):
    match len(arguments):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            if not arguments[1].endswith(".py"):
                sys.exit("Not a Python file")
            return arguments[1]
        case _:
            sys.exit("Too many command-line arguments")


def count_lines(file):
    try:
        with open(file) as file:
            counter = 0
            for line in file:
                line = line.lstrip()
                if line.startswith("#") or line == "" or line == "\n":
                    pass
                else:
                    counter += 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()