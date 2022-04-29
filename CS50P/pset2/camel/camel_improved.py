def main():
    while True:
        user_input = input("CamelCase (blank to exit): ").strip()
        if user_input == "":
            print("Thanks for testing my script. Exiting.")
            break
        else:
            print(convert_to_snake_case(user_input))


def convert_to_snake_case(name):
    snake_case_name = ""
    for c in name:
        if c.isupper():
            c = f"_{c.lower()}"
        snake_case_name += c
    return snake_case_name


def convert_to_snake_case_worse(name):
    for c in name:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")
    return ""


if __name__ == "__main__":
    main()