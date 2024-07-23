# Functions are assigned as elements of a list and then called.


def func1():
    return (60, 7, 91)


def func2():
    return 'woqvg'


def func3():
    return {'xpsll': 49, 'snppb': 8, 'yrtly': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 20


b = ["Hello"]
b[0] = func4

f = b[0]()
