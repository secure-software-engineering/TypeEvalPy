# Functions are assigned as elements of a list and then called.


def func1():
    return [59, 74, 95]


def func2():
    return 91


def func3():
    return {'zknig': 62, 'gquvi': 27, 'eikfw': 32}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'fafal'


b = ["Hello"]
b[0] = func4

f = b[0]()
