import emoji


def main():
    user_input = input("Input: ")
    emojized_input = emoji.emojize(user_input, language="alias")
    print(emojized_input)


if __name__ == "__main__":
    main()