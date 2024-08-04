# Functions are assigned as elements of a list and then called.


def func1():
    return 'fquvw'


def func2():
    return {'fbhtc': 28, 'gpzov': 64, 'xhnos': 93}


def func3():
    return 5.55


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [97, 12, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
