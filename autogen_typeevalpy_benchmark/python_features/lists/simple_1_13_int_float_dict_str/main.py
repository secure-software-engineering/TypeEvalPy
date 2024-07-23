# Functions are assigned as elements of a list and then called.


def func1():
    return 41


def func2():
    return 77.01


def func3():
    return {'ourip': 63, 'mnngy': 99, 'vtaws': 9}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'pyqkd'


b = ["Hello"]
b[0] = func4

f = b[0]()
