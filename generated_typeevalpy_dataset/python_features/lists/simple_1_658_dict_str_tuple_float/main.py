# Functions are assigned as elements of a list and then called.


def func1():
    return {'hdizj': 39, 'ajjob': 96, 'fiwoy': 90}


def func2():
    return 'ymkai'


def func3():
    return (39, 90, 100)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 1.91


b = ["Hello"]
b[0] = func4

f = b[0]()
