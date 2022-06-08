import inflect


def main():
    inflect_engine = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    print(f"Adieu, adieu, to {inflect_engine.join(names)}")


if __name__ == "__main__":
    main()