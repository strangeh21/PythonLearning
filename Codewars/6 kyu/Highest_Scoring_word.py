# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.

characters_value = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k":11, "l": 12, "m": 13, "n":14, "o":15, "p": 16, "q": 17, "r": 18, "s": 19, "t":20, "u":21, "v":22, "w": 23, "x": 24, "y": 25, "z": 26}


def high(x):
    x_list = x.split(" ")
    x_worth = {}
    for word in x_list:
        word_worth = 0
        for character in word:
            character_value = characters_value.get(character)
            word_worth += character_value
        x_worth[word] = word_worth
    highest_word_worth = max(x_worth, key=x_worth.get)
    return highest_word_worth

