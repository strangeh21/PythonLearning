import sys
import csv
from tabulate import tabulate


def main():
    csv_file = read_csv(check_arguments(sys.argv))
    print(tabulated_file(csv_file))


def tabulated_file(file):
    return tabulate(file, headers="firstrow", tablefmt="grid")


def read_csv(file):
    try:
        csv_list = []
        with open(file) as file:
            csv_contents = csv.reader(file, delimiter=",")
            for row in csv_contents:
                csv_list.append(row)
        return csv_list
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments(arguments):
    match len(arguments):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            if arguments[1][-4:] != ".csv":
                sys.exit("Not a CSV file")
            return arguments[1]
        case _:
            sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()