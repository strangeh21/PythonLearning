def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        while True:
            inserted_coin = input("Insert coin: ").strip()
            if inserted_coin == "":
                exit()
            try:
                inserted_coin = int(inserted_coin)
            except ValueError:
                print("Enter a number dummy.")
            else:
                break
        match inserted_coin:
            case (5 | 10 | 25):
                amount_due = subtract_balance(amount_due, inserted_coin)
            case _:
                pass
    print(f"Change owed: {abs(amount_due)}")


def subtract_balance(balance, amount):
    amount_owed = balance - amount
    return amount_owed

if __name__ == "__main__":
    main()