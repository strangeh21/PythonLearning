# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    number = abs(number)
    last_digit = number % 10
    if last_digit == 1 or last_digit == 3 or last_digit == 5 or last_digit == 7 or last_digit == 9:
        return "Odd"
    else:
        return "Even"


def even_or_odd_v2(number):
    if number % 2:
        return "Odd"
    else:
        return "Even"