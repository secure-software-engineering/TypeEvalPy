# Functions are assigned as elements of a list and then called.


def func1():
    return 46.15


def func2():
    return {'taboh': 77, 'aswrf': 13, 'uryiu': 40}


def func3():
    return 14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (41, 84, 74)


b = ["Hello"]
b[0] = func4

f = b[0]()
