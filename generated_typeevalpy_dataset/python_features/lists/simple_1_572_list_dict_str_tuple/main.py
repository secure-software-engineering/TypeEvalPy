# Functions are assigned as elements of a list and then called.


def func1():
    return [8, 55, 47]


def func2():
    return {'owkgm': 90, 'ptklj': 19, 'fffyf': 14}


def func3():
    return 'fhvld'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (57, 94, 11)


b = ["Hello"]
b[0] = func4

f = b[0]()
