# Functions are assigned as elements of a list and then called.


def func1():
    return {'dgtxq': 100, 'zneow': 58, 'jsazn': 63}


def func2():
    return 66.24


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'nlooe'


b = ["Hello"]
b[0] = func4

f = b[0]()
