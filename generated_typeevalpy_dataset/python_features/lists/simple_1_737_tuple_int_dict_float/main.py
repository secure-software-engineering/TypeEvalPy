# Functions are assigned as elements of a list and then called.


def func1():
    return (28, 87, 61)


def func2():
    return 49


def func3():
    return {'upxxd': 37, 'cnruz': 2, 'eolcj': 73}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 23.45


b = ["Hello"]
b[0] = func4

f = b[0]()
