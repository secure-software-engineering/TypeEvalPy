# Functions are assigned as elements of a list and then called.


def func1():
    return 5.71


def func2():
    return [47, 23, 98]


def func3():
    return {'vvrrr': 92, 'dwegv': 45, 'yosmy': 82}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
