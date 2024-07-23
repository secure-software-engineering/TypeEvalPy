# Functions are assigned as elements of a list and then called.


def func1():
    return 'wafzf'


def func2():
    return 5


def func3():
    return [81, 80, 61]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kffnm': 17, 'qleos': 68, 'emuyz': 16}


b = ["Hello"]
b[0] = func4

f = b[0]()
