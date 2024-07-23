# A new list is created as a slice of another one containing functions.


def func1():
    return 4


def func2():
    return 'laprv'


def func3():
    return 24.46


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
