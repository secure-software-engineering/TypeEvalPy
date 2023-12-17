# A program to demonstrate the use of augmented assignments.
# Augmented assignments are used to assign the result of func1


def func1(a):
    a += 3
    a *= 2
    return a


b = func1(5)
