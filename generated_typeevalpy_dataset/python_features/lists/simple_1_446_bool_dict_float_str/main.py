# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'ogpdn': 4, 'mongk': 78, 'rsueb': 13}


def func3():
    return 36.72


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cwndx'


b = ["Hello"]
b[0] = func4

f = b[0]()