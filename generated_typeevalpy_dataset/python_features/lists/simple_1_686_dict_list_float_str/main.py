# Functions are assigned as elements of a list and then called.


def func1():
    return {'pkyxr': 26, 'stxnx': 45, 'rrvmv': 54}


def func2():
    return [48, 52, 1]


def func3():
    return 13.69


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wqzsy'


b = ["Hello"]
b[0] = func4

f = b[0]()
