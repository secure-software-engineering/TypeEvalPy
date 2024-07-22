# Functions are assigned as elements of a list and then called.


def func1():
    return [99, 33, 3]


def func2():
    return 93


def func3():
    return {'nhkjl': 69, 'xobxi': 4, 'avzay': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 70.48


b = ["Hello"]
b[0] = func4

f = b[0]()
