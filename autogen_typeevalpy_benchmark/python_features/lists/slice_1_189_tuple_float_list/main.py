# A new list is created as a slice of another one containing functions.


def func1():
    return (62, 38, 77)


def func2():
    return 88.38


def func3():
    return [3, 99, 61]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
