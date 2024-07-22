# Functions are assigned as elements of a list and then called.


def func1():
    return [16, 54, 64]


def func2():
    return {'cxfhz': 7, 'biqgs': 39, 'qnokg': 42}


def func3():
    return 'gpszd'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 71.15


b = ["Hello"]
b[0] = func4

f = b[0]()
