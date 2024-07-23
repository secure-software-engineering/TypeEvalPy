# Functions are assigned as elements of a list and then called.


def func1():
    return {'mzlyr': 48, 'aysoi': 48, 'vfani': 15}


def func2():
    return 'gwqfq'


def func3():
    return (7, 99, 71)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 2.85


b = ["Hello"]
b[0] = func4

f = b[0]()
