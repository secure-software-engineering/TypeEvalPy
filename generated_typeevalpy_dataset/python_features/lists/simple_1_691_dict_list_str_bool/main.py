# Functions are assigned as elements of a list and then called.


def func1():
    return {'wxrfw': 39, 'ojauu': 95, 'pbwfg': 89}


def func2():
    return [71, 57, 4]


def func3():
    return 'jrfxo'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
