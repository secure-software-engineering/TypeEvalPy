# Functions are assigned as elements of a list and then called.


def func1():
    return 82


def func2():
    return {'upobj': 4, 'kqdso': 87, 'oesll': 65}


def func3():
    return (82, 55, 90)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 78.69


b = ["Hello"]
b[0] = func4

f = b[0]()
