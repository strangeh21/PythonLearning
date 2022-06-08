from plates import is_valid


def main():
    test_plates_true()
    test_plates_begins_alphabetical()
    test_plates_length()
    test_plates_number_placement()
    test_plates_zero()
    test_plates_alphanumeric()


def test_plates_true():
    assert is_valid("CS50")
    assert is_valid("eth")
    assert is_valid("magic1")
    assert is_valid("plate9")
    assert is_valid("play58")
    assert is_valid("ab")


def test_plates_begins_alphabetical():
    assert is_valid("50s") is False
    assert is_valid("a501") is False
    assert is_valid("b109") is False


def test_plates_length():
    assert is_valid("a") is False
    assert is_valid("ab50501") is False
    assert is_valid("charlie105") is False
    assert is_valid("hahaha10") is False


def test_plates_number_placement():
    assert is_valid("ab50h") is False
    assert is_valid("abc50a") is False


def test_plates_zero():
    assert is_valid("ab05") is False
    assert is_valid("play01") is False


def test_plates_alphanumeric():
    assert is_valid("$£50") is False
    assert is_valid("CS#¤!") is False
    assert is_valid("AP!50") is False



if __name__ == "__main__":
    main()
