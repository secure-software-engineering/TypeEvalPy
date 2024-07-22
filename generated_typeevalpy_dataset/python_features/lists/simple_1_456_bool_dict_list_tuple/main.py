# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'hxfou': 72, 'svmdh': 15, 'etsch': 86}


def func3():
    return [25, 57, 28]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (56, 27, 91)


b = ["Hello"]
b[0] = func4

f = b[0]()
