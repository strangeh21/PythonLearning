from bank import value


def main():
    test_bank()


def test_bank():
    assert value("Hello, buddy!") == 0
    assert value("hey, buddy") == 20
    assert value("what's up") == 100
    assert value("") == 100


if __name__ == "__main__":
    main()