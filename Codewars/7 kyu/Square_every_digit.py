# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    num_list = list(str(num))
    squared_list = []
    string_number = ""
    for i in num_list:
        i = int(i)
        squared_list.append(i*i)
    for i in squared_list:
        i = str(i)
        string_number += i
    string_number = int(string_number)
    return string_number