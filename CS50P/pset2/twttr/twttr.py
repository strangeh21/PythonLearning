def main():
    user_input = input("Input (Blank to exit): ").strip()
    print("Thanks for testing my script. Exiting.")
    print(omit_vowels(user_input))


def omit_vowels(input):
    output = ""
    for c in input:
        match c:
            case ("a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U"):
                pass
            case _:
                output += c
    return output


if __name__ == "__main__":
    main()