# Functions are assigned as elements of a list and then called.


def func1():
    return {'hfoep': 19, 'dzwlh': 19, 'rgfzq': 94}


def func2():
    return 'aubwc'


def func3():
    return 79.14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (68, 95, 56)


b = ["Hello"]
b[0] = func4

f = b[0]()
