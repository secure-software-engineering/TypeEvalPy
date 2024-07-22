# Functions are assigned as elements of a list and then called.


def func1():
    return 'npxxv'


def func2():
    return {'zzvyp': 46, 'yhfog': 53, 'qzope': 91}


def func3():
    return 67


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [59, 62, 86]


b = ["Hello"]
b[0] = func4

f = b[0]()
