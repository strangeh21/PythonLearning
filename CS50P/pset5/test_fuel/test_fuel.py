from fuel import gauge, convert
import pytest


def main():
    test_fuel_convert_correct()
    test_fuel_convert_zerodivision()
    test_fuel_convert_valueerror()
    test_fuel_gauge_empty()
    test_fuel_gauge_full()
    test_fuel_gauge_int()


def test_fuel_convert_correct():
    assert convert("3/4") == 75
    assert convert("500/1000") == 50
    assert convert("350/1000") == 35
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("99/100") == 99


def test_fuel_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
        convert("999/0")
        convert("856/0")


def test_fuel_convert_valueerror():
    with pytest.raises(ValueError):
        convert("hey/hello")
        convert("one/100")
        convert("10/hundred")


def test_fuel_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_fuel_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_fuel_gauge_int():
    assert gauge(59) == "59%"
    assert gauge(32) == "32%"
    assert gauge(98) == "98%"
    assert gauge(49) == "49%"


if __name__ == "__main__":
    main()