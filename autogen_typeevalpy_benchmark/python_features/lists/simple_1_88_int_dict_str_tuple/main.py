# Functions are assigned as elements of a list and then called.


def func1():
    return 11


def func2():
    return {'wbeeg': 44, 'tcarg': 50, 'ttrrd': 33}


def func3():
    return 'mkvis'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (60, 53, 57)


b = ["Hello"]
b[0] = func4

f = b[0]()
