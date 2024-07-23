# A new list is created as a slice of another one containing functions.


def func1():
    return 7.08


def func2():
    return [91, 90, 87]


def func3():
    return 19


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
