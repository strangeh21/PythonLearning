import sys
import requests


def main():
    arguments = sys.argv
    match len(arguments):
        case 1:
            sys.exit("Missing command-line argument")
        case 2:
            user_input_float = ConvertToFloat(sys.argv[1])
            if not user_input_float:
                sys.exit("Command-line argument is not a number")
        case _:
            sys.exit("Too many arguments")
    current_price = get_current_price()
    print(f"${GetWorth(user_input_float, current_price):,.4f}")


def get_current_price():
    try:
        coindesk_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        return coindesk_json["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Failed to get BTC price from coindesk.")


def ConvertToFloat(number):
    try:
        number = float(number)
        return number
    except ValueError:
        return False


def GetWorth(amount, price):
    return amount * price


if __name__ == "__main__":
    main()