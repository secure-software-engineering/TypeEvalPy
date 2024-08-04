# A new list is created as a slice of another one containing functions.


def func1():
    return 'ucdtu'


def func2():
    return [75, 81, 21]


def func3():
    return 82.11


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
