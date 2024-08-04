# Functions are assigned as elements of a list and then called.


def func1():
    return [7, 17, 50]


def func2():
    return (81, 66, 59)


def func3():
    return {'vrinx': 94, 'aftno': 16, 'iienm': 58}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 21


b = ["Hello"]
b[0] = func4

f = b[0]()
