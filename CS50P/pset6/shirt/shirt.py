import os
import sys
from PIL import Image
from PIL import ImageOps


def main():
    profile_loc, output_loc = check_arguments(sys.argv)
    shirt_overlay = "shirt.png"
    if not check_file_exist(profile_loc):
        sys.exit("Input does not exist")
    if not check_file_exist(shirt_overlay):
        sys.exit("Missing shirt.png")
    new_profile_pic = add_overlay(profile_loc, shirt_overlay)
    Image.Image.save(new_profile_pic, output_loc)


def check_arguments(arguments):
    match len(arguments):
        case (1 | 2):
            sys.exit("Too few command-line arguments")
        case 3:
            arg1, arg1ext = os.path.splitext(arguments[1])
            arg2, arg2ext = os.path.splitext(arguments[2])
            if arg1ext not in [".jpg", ".jpeg", ".png"]:
                sys.exit("Argument 1 is not png, jpg or jpeg")
            elif arg2ext not in [".jpg", ".jpeg", ".png"]:
                sys.exit("Argument 2 is not png, jpg or jpeg")
            elif arg1ext != arg2ext:
                sys.exit("Input and output have different extensions")
            return arguments[1], arguments[2]
        case _:
            sys.exit("Too many command-line arguments")


def check_file_exist(path):
    return os.path.isfile(path)


def add_overlay(profile_pic, overlay):
    profile_pic = Image.open(profile_pic)
    overlay = Image.open(overlay)
    overlay_size = overlay.size
    profile_pic = ImageOps.fit(profile_pic, overlay_size)
    profile_pic.paste(overlay, (0, 0), overlay)
    return profile_pic


if __name__ == "__main__":
    main()
