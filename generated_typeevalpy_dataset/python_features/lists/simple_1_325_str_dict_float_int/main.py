# Functions are assigned as elements of a list and then called.


def func1():
    return 'olzde'


def func2():
    return {'ywdbs': 59, 'zinjn': 32, 'fymrn': 20}


def func3():
    return 13.55


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 50


b = ["Hello"]
b[0] = func4

f = b[0]()
