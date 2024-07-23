# A new list is created as a slice of another one containing functions.


def func1():
    return 'otrni'


def func2():
    return 72


def func3():
    return (64, 67, 48)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
