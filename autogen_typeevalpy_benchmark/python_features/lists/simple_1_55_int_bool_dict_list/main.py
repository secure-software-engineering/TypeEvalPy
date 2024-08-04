# Functions are assigned as elements of a list and then called.


def func1():
    return 20


def func2():
    return False


def func3():
    return {'sozzf': 65, 'ijgav': 7, 'ewscq': 8}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [19, 11, 96]


b = ["Hello"]
b[0] = func4

f = b[0]()
