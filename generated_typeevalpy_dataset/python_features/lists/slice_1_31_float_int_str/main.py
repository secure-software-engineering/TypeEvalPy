# A new list is created as a slice of another one containing functions.


def func1():
    return 64.87


def func2():
    return 46


def func3():
    return 'jmtzb'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
