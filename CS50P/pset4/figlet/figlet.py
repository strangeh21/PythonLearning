import sys
import pyfiglet
import random


def Main():
    figlet = pyfiglet.Figlet()
    font_list = figlet.getFonts()
    if CheckArgument(sys.argv):
        if not CheckFontInList(sys.argv[2], font_list):
            sys.exit("Font does not exist.")
        figlet.setFont(font=sys.argv[2])
    else:
        figlet.setFont(font=random.choice(font_list))
    word_to_convert = input("Input: ")
    print(figlet.renderText(word_to_convert))


# Check if Argument is in right order. Return true if 2 arguments with correct start. Return false if none.
def CheckArgument(argv):
    match len(argv):
        case 1:
            return False
        case 3:
            match argv[1]:
                case ("-f" | "--font"):
                    return True
                case _:
                    sys.exit("Incorrect argument used. Please use '-f' or '--font'.")
        case _:
            sys.exit("Not the right number of arguments. Either none or 2.")


def CheckFontInList(font, fontlist):
    return font in fontlist


if __name__ == "__main__":
    Main()