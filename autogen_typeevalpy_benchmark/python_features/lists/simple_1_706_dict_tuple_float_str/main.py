# Functions are assigned as elements of a list and then called.


def func1():
    return {'nzzco': 32, 'fproe': 64, 'pejnr': 94}


def func2():
    return (37, 58, 68)


def func3():
    return 91.93


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wndiq'


b = ["Hello"]
b[0] = func4

f = b[0]()
