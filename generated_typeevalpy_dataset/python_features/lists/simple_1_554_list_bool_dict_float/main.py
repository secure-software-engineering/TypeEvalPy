# Functions are assigned as elements of a list and then called.


def func1():
    return [3, 94, 5]


def func2():
    return True


def func3():
    return {'bdgcr': 75, 'ltvrm': 41, 'bvoub': 55}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 48.57


b = ["Hello"]
b[0] = func4

f = b[0]()
