# Functions are assigned as elements of a list and then called.


def func1():
    return {'bqibd': 74, 'eswbd': 20, 'nqlmr': 72}


def func2():
    return [82, 8, 74]


def func3():
    return 6


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
