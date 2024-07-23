# Functions are assigned as elements of a list and then called.


def func1():
    return 27


def func2():
    return False


def func3():
    return {'tomfg': 86, 'fhyvj': 21, 'aowjs': 90}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 65.03


b = ["Hello"]
b[0] = func4

f = b[0]()
