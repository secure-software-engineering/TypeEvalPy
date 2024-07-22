# Functions are assigned as elements of a list and then called.


def func1():
    return (45, 25, 75)


def func2():
    return {'usbtp': 79, 'qxiir': 97, 'lcwnt': 87}


def func3():
    return [75, 34, 92]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 16


b = ["Hello"]
b[0] = func4

f = b[0]()
