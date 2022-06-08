import sys
import csv
import os


def main():
    input_file, output_file = check_arguments(sys.argv)
    converted_csv_output = convert_csv(input_file)
    export_csv(converted_csv_output, output_file)


def export_csv(converted_csv_contents, output_location):
    if os.path.isfile(output_location):
        mode = "w"
    else:
        mode = "x"
    with open(output_location, mode, newline="") as new_csv_file:
        new_csv = csv.writer(new_csv_file)
        new_csv.writerow(["first", "last", "house"])
        new_csv.writerows(converted_csv_contents)


def convert_csv(file):
    try:
        csv_list = []
        with open(file) as file:
            csv_contents = csv.reader(file, delimiter=",")
            next(csv_contents)
            for row in csv_contents:
                last, first = row[0].split(", ")
                row = [first, last, row[1]]
                csv_list.append(row)
        return csv_list
    except FileNotFoundError:
        sys.exit(f"Could not read {file}")


def check_arguments(arguments):
    match len(arguments):
        case (1 | 2):
            sys.exit("Too few command-line arguments")
        case 3:
            if arguments[1][-4:] != ".csv" and arguments[2][-4:] != ".csv":
                sys.exit("One or more of the argu")
            return arguments[1], arguments[2]
        case _:
            sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()