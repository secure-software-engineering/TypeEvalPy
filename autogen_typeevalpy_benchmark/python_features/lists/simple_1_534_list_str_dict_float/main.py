# Functions are assigned as elements of a list and then called.


def func1():
    return [92, 42, 100]


def func2():
    return 'unpin'


def func3():
    return {'pstio': 60, 'oytcc': 41, 'kmtaj': 82}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 64.26


b = ["Hello"]
b[0] = func4

f = b[0]()
