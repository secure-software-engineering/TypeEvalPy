# Functions are assigned as elements of a list and then called.


def func1():
    return 'seyzx'


def func2():
    return {'atdwd': 71, 'bpkcx': 60, 'tlohb': 60}


def func3():
    return [56, 87, 70]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61.49


b = ["Hello"]
b[0] = func4

f = b[0]()
