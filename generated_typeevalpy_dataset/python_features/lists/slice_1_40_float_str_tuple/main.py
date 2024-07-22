# A new list is created as a slice of another one containing functions.


def func1():
    return 10.11


def func2():
    return 'yxwva'


def func3():
    return (64, 26, 30)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
