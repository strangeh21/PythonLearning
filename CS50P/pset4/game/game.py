import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            break
        except ValueError:
            pass
    randnum = GenerateRandomNumber(1, level)
    print(randnum)
    while True:
        try:
            guess = int(input("Guess: "))
            is_same = IsNumSame(randnum, guess)
            match is_same:
                case "Just right!":
                    print(is_same)
                    break
                case _:
                    print(is_same)
            #match guess:
            #    case guess if guess < randnum:
            #        print("Too small!")
            #    case guess if guess > randnum:
            #        print("Too large!")
            #    case _:
            #        print("Just right!")
            #        break
        except ValueError:
            pass


def GenerateRandomNumber(minimum, maximum):
    return random.randint(minimum, maximum)


# Another way of doing it.
def IsNumSame(randomnumber, guess):
    if guess == randomnumber:
        return "Just right!"
    elif guess < randomnumber:
        return "Too small!"
    elif guess > randomnumber:
        return "Too large!"
    else:
        raise ValueError("Numbers do not make sense. Not the same, not larger or smaller.")


if __name__ == "__main__":
    main()