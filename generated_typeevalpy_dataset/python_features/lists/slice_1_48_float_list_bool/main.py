# A new list is created as a slice of another one containing functions.


def func1():
    return 47.85


def func2():
    return [63, 5, 96]


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
