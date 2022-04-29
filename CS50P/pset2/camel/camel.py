def main():
    user_input = input("CamelCase: ").strip()
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