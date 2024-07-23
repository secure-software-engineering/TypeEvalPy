# Functions are assigned as elements of a list and then called.


def func1():
    return [83, 24, 42]


def func2():
    return 'qbdgh'


def func3():
    return 37.73


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'miswt': 55, 'fjrkh': 13, 'kknog': 61}


b = ["Hello"]
b[0] = func4

f = b[0]()
