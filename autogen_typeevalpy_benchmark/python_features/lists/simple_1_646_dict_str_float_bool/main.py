# Functions are assigned as elements of a list and then called.


def func1():
    return {'gbaxe': 62, 'whnep': 37, 'udzju': 33}


def func2():
    return 'ykxsv'


def func3():
    return 15.31


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
