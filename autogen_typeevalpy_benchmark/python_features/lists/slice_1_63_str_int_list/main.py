# A new list is created as a slice of another one containing functions.


def func1():
    return 'mikzq'


def func2():
    return 95


def func3():
    return [37, 44, 59]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
