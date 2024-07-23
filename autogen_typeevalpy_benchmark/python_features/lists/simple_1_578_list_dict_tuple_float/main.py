# Functions are assigned as elements of a list and then called.


def func1():
    return [63, 39, 67]


def func2():
    return {'pxlep': 74, 'gekrw': 84, 'rhjhz': 77}


def func3():
    return (80, 7, 14)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 90.48


b = ["Hello"]
b[0] = func4

f = b[0]()
