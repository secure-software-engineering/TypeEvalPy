# A program to demonstrate the use of augmented assignments.
# Augmented assignments are used to assign the result of func1


def func1(a):
    a += [13, 85, 56]
    return a


b = func1([13, 85, 56])
