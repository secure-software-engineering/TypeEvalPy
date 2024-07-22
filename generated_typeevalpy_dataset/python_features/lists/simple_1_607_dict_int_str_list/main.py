# Functions are assigned as elements of a list and then called.


def func1():
    return {'brqin': 65, 'euzkv': 73, 'gvasn': 13}


def func2():
    return 48


def func3():
    return 'ykrqw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [44, 80, 34]


b = ["Hello"]
b[0] = func4

f = b[0]()
