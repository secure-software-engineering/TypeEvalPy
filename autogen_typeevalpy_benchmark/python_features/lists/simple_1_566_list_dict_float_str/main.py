# Functions are assigned as elements of a list and then called.


def func1():
    return [100, 18, 28]


def func2():
    return {'sehjf': 72, 'micuk': 38, 'gngpe': 16}


def func3():
    return 32.24


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'gnlxs'


b = ["Hello"]
b[0] = func4

f = b[0]()
