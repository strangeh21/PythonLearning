# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    text_list = text[::-1].split(" ")
    text_list.reverse()
    text_list_reversed_words = ""
    for word in text_list:
        text_list_reversed_words += word + " "
    return text_list_reversed_words.strip()