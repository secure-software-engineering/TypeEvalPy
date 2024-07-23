# A new list is created as a slice of another one containing functions.


def func1():
    return {'qmzfq': 4, 'xdxuc': 32, 'bbvqt': 82}


def func2():
    return 35.85


def func3():
    return (67, 62, 71)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
