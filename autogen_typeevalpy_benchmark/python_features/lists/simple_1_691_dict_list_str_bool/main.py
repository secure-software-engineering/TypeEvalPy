# Functions are assigned as elements of a list and then called.


def func1():
    return {'yvcun': 8, 'ajfqd': 46, 'ffldu': 15}


def func2():
    return [55, 94, 15]


def func3():
    return 'buyle'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
