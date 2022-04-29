# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example:
#
# 348597 => [7,9,5,8,4,3]
# 0 => [0]

def digitize(n):
    n = list(str(n))
    n = [int(x) for x in n]
    n.reverse()
    return n

def digitize_better(n):
    n = list(str(n)[::-1])
    n = [int(x) for x in n]
    return n