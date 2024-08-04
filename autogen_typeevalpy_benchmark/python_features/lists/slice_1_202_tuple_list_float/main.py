# A new list is created as a slice of another one containing functions.


def func1():
    return (1, 34, 46)


def func2():
    return [80, 64, 64]


def func3():
    return 77.59


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
