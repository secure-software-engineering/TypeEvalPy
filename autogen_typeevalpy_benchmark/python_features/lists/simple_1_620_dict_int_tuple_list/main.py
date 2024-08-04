# Functions are assigned as elements of a list and then called.


def func1():
    return {'dcdkb': 41, 'pnwsu': 34, 'dablo': 60}


def func2():
    return 11


def func3():
    return (32, 29, 18)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [86, 42, 71]


b = ["Hello"]
b[0] = func4

f = b[0]()
