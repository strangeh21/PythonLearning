# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    word_list = s.split(" ")
    length_of_items = []
    for i in word_list:
        length_of_items.append(len(i))
    length_of_items.sort()
    l = length_of_items[0]
    print(word_list)
    return l # l: shortest word length