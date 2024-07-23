# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'finkx': 86, 'avcbo': 29, 'gxhgc': 83}


def func3():
    return 79.39


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (45, 7, 29)


b = ["Hello"]
b[0] = func4

f = b[0]()
