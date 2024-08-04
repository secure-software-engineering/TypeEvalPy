# Functions are assigned as elements of a list and then called.


def func1():
    return {'ahsrd': 1, 'jtqdk': 1, 'jhlrw': 69}


def func2():
    return 66


def func3():
    return 'onzmk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (96, 14, 40)


b = ["Hello"]
b[0] = func4

f = b[0]()
