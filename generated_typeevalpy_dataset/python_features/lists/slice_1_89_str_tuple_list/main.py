# A new list is created as a slice of another one containing functions.


def func1():
    return 'vbanv'


def func2():
    return (59, 40, 13)


def func3():
    return [11, 90, 56]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
