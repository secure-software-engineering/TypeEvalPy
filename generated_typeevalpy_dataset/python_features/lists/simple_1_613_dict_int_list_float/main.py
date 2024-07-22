# Functions are assigned as elements of a list and then called.


def func1():
    return {'ggbwm': 25, 'frpki': 95, 'sftcp': 82}


def func2():
    return 100


def func3():
    return [22, 77, 98]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 5.51


b = ["Hello"]
b[0] = func4

f = b[0]()
