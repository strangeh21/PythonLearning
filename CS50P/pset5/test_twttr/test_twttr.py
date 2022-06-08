from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("Hello, My NAmE is Eirik.") == "Hll, My Nm s rk."
    assert shorten("hello, my name is eirik.") == "hll, my nm s rk."
    assert shorten("Twitter") == "Twttr"
    assert shorten("aaaaaaaaaa") == ""
    assert shorten("aaaaaaabaaaaEEEIoIIiiO") == "b"
    assert shorten("CS50P and CS50p") == "CS50P nd CS50p"


if __name__ == "__main__":
    main()