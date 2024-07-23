# Functions are assigned as elements of a list and then called.


def func1():
    return (22, 43, 21)


def func2():
    return 'gjhnt'


def func3():
    return 99


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'iwogw': 44, 'eecmb': 68, 'wshvu': 14}


b = ["Hello"]
b[0] = func4

f = b[0]()
