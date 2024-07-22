# Functions are assigned as elements of a list and then called.


def func1():
    return [72, 51, 95]


def func2():
    return 70.1


def func3():
    return {'igxtb': 17, 'arowo': 68, 'lmtgz': 56}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'jkafz'


b = ["Hello"]
b[0] = func4

f = b[0]()
