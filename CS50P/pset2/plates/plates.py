def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6: # If length is lower than 2 or higher than 6
        return False
    if not s.isalnum():
        return False
    for c in s[0:2]: # If first 2 characters are not in alphabet
        if not c.lower().isalpha():
            return False
    counter = 2
    for c in s[2:]: # if s contains digit, split at first number and check if end contains alphabet.
        if c.isdigit():
            s_digit_split = s[counter:]
            if s_digit_split[:1] == "0":
                return False
            if not s_digit_split.isdigit(): # If end_of_s contains letter
                return False
            break
        counter += 1
    return True


if __name__ == "__main__":
    main()
