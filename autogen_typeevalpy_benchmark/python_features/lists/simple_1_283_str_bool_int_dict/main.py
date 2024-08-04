# Functions are assigned as elements of a list and then called.


def func1():
    return 'pbpxg'


def func2():
    return False


def func3():
    return 6


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rvsbn': 57, 'mynrk': 50, 'irejw': 67}


b = ["Hello"]
b[0] = func4

f = b[0]()
