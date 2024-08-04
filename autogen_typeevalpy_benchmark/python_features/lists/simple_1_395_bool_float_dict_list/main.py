# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 19.92


def func3():
    return {'rtisn': 60, 'visge': 94, 'vlyft': 98}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [64, 26, 30]


b = ["Hello"]
b[0] = func4

f = b[0]()
