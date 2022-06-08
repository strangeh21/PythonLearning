def main():
    user_input = input("Input (Blank to exit): ").strip()
    print("Thanks for testing my script. Exiting.")
    print(shorten(user_input))


def shorten(word):
    output = ""
    for c in word:
        match c.lower():
            case ("a" | "e" | "i" | "o" | "u"):
                pass
            case _:
                output += c
    return output


if __name__ == "__main__":
    main()