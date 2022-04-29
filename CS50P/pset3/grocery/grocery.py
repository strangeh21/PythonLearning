def main():
    shopping_list = {}
    while True:
        try:
            user_input = input("").upper()
            if user_input in shopping_list:
                shopping_list[user_input] += 1
            else:
                shopping_list[user_input] = 1
        except EOFError:
            shopping_list_items = sorted(shopping_list.keys())
            for i in shopping_list_items:
                print(f"{shopping_list[i]} {i}")
            break

if __name__ == "__main__":
    main()