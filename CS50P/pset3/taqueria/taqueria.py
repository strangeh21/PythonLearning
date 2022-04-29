menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total_bill = 0
    while True:
        try:
            item = input("Item: ").title()
            # item_price = menu.get(item)
            # total_bill += item_price
            if item in menu:
                total_bill += menu[item]
        except (KeyError, TypeError):
            pass
        except EOFError:
            break
        print(f"Total: ${total_bill:.2f}")
    print(f"Total: ${total_bill:.2f}")


if __name__ == "__main__":
    main()