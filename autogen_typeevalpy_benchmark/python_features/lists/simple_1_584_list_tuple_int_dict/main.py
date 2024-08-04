# Functions are assigned as elements of a list and then called.


def func1():
    return [70, 65, 37]


def func2():
    return (40, 6, 94)


def func3():
    return 99


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'dguae': 34, 'frucq': 94, 'jwdrg': 22}


b = ["Hello"]
b[0] = func4

f = b[0]()
