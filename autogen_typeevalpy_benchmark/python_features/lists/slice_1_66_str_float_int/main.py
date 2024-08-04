# A new list is created as a slice of another one containing functions.


def func1():
    return 'fweky'


def func2():
    return 42.47


def func3():
    return 80


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
