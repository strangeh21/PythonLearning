# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    list_of_lengths = [a, b, c]
    list_of_lengths.sort()
    if list_of_lengths[0] + list_of_lengths[1] <= list_of_lengths[2]:
        return False
    else:
        return True