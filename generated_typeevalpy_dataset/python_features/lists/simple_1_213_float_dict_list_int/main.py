# Functions are assigned as elements of a list and then called.


def func1():
    return 44.74


def func2():
    return {'fjqfe': 38, 'heoyj': 68, 'lyjju': 50}


def func3():
    return [98, 41, 44]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 44


b = ["Hello"]
b[0] = func4

f = b[0]()
