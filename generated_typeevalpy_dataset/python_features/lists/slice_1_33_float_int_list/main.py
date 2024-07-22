# A new list is created as a slice of another one containing functions.


def func1():
    return 17.53


def func2():
    return 56


def func3():
    return [65, 60, 51]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
