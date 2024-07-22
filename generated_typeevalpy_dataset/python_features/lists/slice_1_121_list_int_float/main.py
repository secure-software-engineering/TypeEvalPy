# A new list is created as a slice of another one containing functions.


def func1():
    return [53, 26, 100]


def func2():
    return 87


def func3():
    return 14.64


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
