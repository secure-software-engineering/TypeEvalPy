# Functions are assigned as elements of a list and then called.


def func1():
    return 34


def func2():
    return {'enmct': 100, 'gveei': 99, 'srofm': 22}


def func3():
    return 64.58


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [19, 27, 93]


b = ["Hello"]
b[0] = func4

f = b[0]()
