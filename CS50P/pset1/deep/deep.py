user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

match user_answer:
    case ("42" | "fortytwo" | "forty-two" | "forty two" ):
        print("Yes")
    case _:
        print("No")