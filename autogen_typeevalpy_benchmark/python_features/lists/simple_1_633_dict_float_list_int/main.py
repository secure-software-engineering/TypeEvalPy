# Functions are assigned as elements of a list and then called.


def func1():
    return {'scbgh': 25, 'wxzik': 28, 'owetx': 34}


def func2():
    return 35.11


def func3():
    return [57, 8, 65]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 86


b = ["Hello"]
b[0] = func4

f = b[0]()
