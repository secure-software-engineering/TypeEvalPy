# Functions are assigned as elements of a list and then called.


def func1():
    return 66.87


def func2():
    return [5, 57, 64]


def func3():
    return 30


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'nlssv': 32, 'atlsu': 10, 'tgocs': 66}


b = ["Hello"]
b[0] = func4

f = b[0]()
