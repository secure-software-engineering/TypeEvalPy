# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [79, 34, 23]


def func3():
    return {'jkytn': 28, 'gjxsq': 32, 'ygycl': 23}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (8, 29, 87)


b = ["Hello"]
b[0] = func4

f = b[0]()
