greeting = input("Greeting: ").strip().lower()


match greeting:
    case greeting if greeting[0:5] == "hello":
        print("$0")
    case greeting if greeting[0] == "h":
        print("$20")
    case _:
        print("$100")
