# Functions are assigned as elements of a list and then called.


def func1():
    return 62.0


def func2():
    return 15


def func3():
    return {'zuhvb': 3, 'rjuyj': 58, 'rernb': 39}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'qsewg'


b = ["Hello"]
b[0] = func4

f = b[0]()
