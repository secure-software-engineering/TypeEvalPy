# Functions are assigned as elements of a list and then called.


def func1():
    return {'svonm': 67, 'iutjp': 35, 'dqlgf': 8}


def func2():
    return (65, 83, 60)


def func3():
    return 9


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'omikv'


b = ["Hello"]
b[0] = func4

f = b[0]()
