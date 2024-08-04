# A new list is created as a slice of another one containing functions.


def func1():
    return 80


def func2():
    return False


def func3():
    return 11.13


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
