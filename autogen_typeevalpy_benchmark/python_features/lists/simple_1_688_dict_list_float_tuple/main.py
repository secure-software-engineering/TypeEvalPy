# Functions are assigned as elements of a list and then called.


def func1():
    return {'titww': 53, 'pyqrf': 30, 'tqatf': 33}


def func2():
    return [57, 81, 11]


def func3():
    return 93.65


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (89, 50, 64)


b = ["Hello"]
b[0] = func4

f = b[0]()
