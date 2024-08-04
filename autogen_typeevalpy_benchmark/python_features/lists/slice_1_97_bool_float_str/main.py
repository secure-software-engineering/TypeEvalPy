# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return 6.09


def func3():
    return 'xdmce'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
