# Functions are assigned as elements of a list and then called.


def func1():
    return [85, 51, 19]


def func2():
    return True


def func3():
    return 24.3


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bvsgz': 39, 'nhnyw': 38, 'quqea': 61}


b = ["Hello"]
b[0] = func4

f = b[0]()
