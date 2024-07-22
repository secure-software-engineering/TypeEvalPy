# Functions are assigned as elements of a list and then called.


def func1():
    return 'gesdt'


def func2():
    return 8


def func3():
    return (13, 94, 88)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bdqpt': 34, 'smyqq': 33, 'idqyn': 56}


b = ["Hello"]
b[0] = func4

f = b[0]()
