# A new list is created as a slice of another one containing functions.


def func1():
    return (11, 70, 45)


def func2():
    return 96.04


def func3():
    return 35


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
