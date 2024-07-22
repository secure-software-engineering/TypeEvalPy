# Functions are assigned as elements of a list and then called.


def func1():
    return 32.69


def func2():
    return {'yixkb': 54, 'omxgq': 57, 'bpnwf': 55}


def func3():
    return (11, 70, 23)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [24, 59, 72]


b = ["Hello"]
b[0] = func4

f = b[0]()
