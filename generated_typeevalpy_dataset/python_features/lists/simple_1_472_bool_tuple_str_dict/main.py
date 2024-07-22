# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return (5, 76, 19)


def func3():
    return 'waqis'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'uaxvz': 56, 'gpnrv': 79, 'fgyhf': 73}


b = ["Hello"]
b[0] = func4

f = b[0]()
