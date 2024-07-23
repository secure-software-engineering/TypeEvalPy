# Functions are assigned as elements of a list and then called.


def func1():
    return [79, 34, 24]


def func2():
    return {'swaqi': 99, 'qexqx': 74, 'tujva': 26}


def func3():
    return 33


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 17.61


b = ["Hello"]
b[0] = func4

f = b[0]()
