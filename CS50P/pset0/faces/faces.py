def main():
    user_input = input("Please enter text to be converted: ")
    user_input_converted = convert(user_input)
    print(user_input_converted)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


main()