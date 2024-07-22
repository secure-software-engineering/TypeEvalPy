# Functions are assigned as elements of a list and then called.


def func1():
    return 52.62


def func2():
    return (85, 34, 1)


def func3():
    return {'aglzl': 38, 'cncqr': 55, 'xtgzl': 40}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 41


b = ["Hello"]
b[0] = func4

f = b[0]()
