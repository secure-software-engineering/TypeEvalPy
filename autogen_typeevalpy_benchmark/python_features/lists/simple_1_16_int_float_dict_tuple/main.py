# Functions are assigned as elements of a list and then called.


def func1():
    return 18


def func2():
    return 79.8


def func3():
    return {'zyndi': 42, 'nvbck': 48, 'kdugg': 57}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (19, 40, 64)


b = ["Hello"]
b[0] = func4

f = b[0]()
