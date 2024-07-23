# A new list is created as a slice of another one containing functions.


def func1():
    return 17.54


def func2():
    return [79, 70, 95]


def func3():
    return 'ljcfv'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
