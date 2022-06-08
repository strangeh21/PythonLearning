import random


def main():
    level = get_level()
    points = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        is_correct = False
        for _ in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    points += 1
                    is_correct = True
                    break
                print("EEE")
            except ValueError:
                pass
        if not is_correct:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {points}")


def get_level():
    while True:
        level = input("Level: ")
        match level:
            case ("1" | "2" | "3"):
                return int(level)
            case _:
                pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
