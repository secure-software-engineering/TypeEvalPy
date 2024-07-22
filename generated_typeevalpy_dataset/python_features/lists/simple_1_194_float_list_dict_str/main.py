# Functions are assigned as elements of a list and then called.


def func1():
    return 11.92


def func2():
    return [4, 73, 78]


def func3():
    return {'yekgo': 12, 'inyga': 35, 'vafnt': 41}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'mqwyq'


b = ["Hello"]
b[0] = func4

f = b[0]()
