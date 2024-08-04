# Functions are assigned as elements of a list and then called.


def func1():
    return [6, 12, 18]


def func2():
    return {'tbfjy': 64, 'jpsqp': 49, 'ikjhr': 51}


def func3():
    return 93.62


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'uzsfs'


b = ["Hello"]
b[0] = func4

f = b[0]()
