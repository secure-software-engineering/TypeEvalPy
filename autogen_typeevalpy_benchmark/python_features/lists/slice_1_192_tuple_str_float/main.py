# A new list is created as a slice of another one containing functions.


def func1():
    return (39, 72, 88)


def func2():
    return 'sroox'


def func3():
    return 68.28


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
