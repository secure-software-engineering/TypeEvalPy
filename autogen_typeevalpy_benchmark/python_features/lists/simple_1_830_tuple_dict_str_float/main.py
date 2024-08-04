# Functions are assigned as elements of a list and then called.


def func1():
    return (30, 36, 3)


def func2():
    return {'bdrmk': 81, 'lulgp': 84, 'oiwrs': 55}


def func3():
    return 'cbknw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77.92


b = ["Hello"]
b[0] = func4

f = b[0]()
