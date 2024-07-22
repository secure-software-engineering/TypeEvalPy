# Functions are assigned as elements of a list and then called.


def func1():
    return 73.19


def func2():
    return 'qfxdo'


def func3():
    return {'zxrrs': 27, 'pjujr': 48, 'fujgq': 10}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (37, 53, 4)


b = ["Hello"]
b[0] = func4

f = b[0]()
