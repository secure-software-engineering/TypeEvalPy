# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return (36, 69, 42)


def func3():
    return [32, 11, 44]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'pqutl': 31, 'rkatr': 66, 'vimmm': 98}


b = ["Hello"]
b[0] = func4

f = b[0]()
