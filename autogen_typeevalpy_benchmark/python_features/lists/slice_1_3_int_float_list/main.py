# A new list is created as a slice of another one containing functions.


def func1():
    return 19


def func2():
    return 61.2


def func3():
    return [61, 35, 96]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
