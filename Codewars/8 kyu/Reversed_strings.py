# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    string = list(string)
    string.reverse()
    reversed_string = ""
    for c in string:
        reversed_string += c
    return reversed_string