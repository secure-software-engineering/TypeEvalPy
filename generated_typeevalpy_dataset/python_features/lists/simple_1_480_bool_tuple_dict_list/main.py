# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (36, 8, 28)


def func3():
    return {'xxkcc': 45, 'rrhnn': 27, 'zgbbm': 55}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [70, 46, 25]


b = ["Hello"]
b[0] = func4

f = b[0]()
