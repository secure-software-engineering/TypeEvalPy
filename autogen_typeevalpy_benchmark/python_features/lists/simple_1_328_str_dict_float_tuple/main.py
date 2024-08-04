# Functions are assigned as elements of a list and then called.


def func1():
    return 'gilsv'


def func2():
    return {'ttqsj': 37, 'aedvq': 42, 'qxbfa': 61}


def func3():
    return 88.35


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (92, 1, 85)


b = ["Hello"]
b[0] = func4

f = b[0]()
