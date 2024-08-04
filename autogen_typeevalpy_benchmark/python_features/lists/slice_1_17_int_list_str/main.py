# A new list is created as a slice of another one containing functions.


def func1():
    return 11


def func2():
    return [14, 11, 28]


def func3():
    return 'afkct'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
