# Functions are assigned as elements of a list and then called.


def func1():
    return 'oicpb'


def func2():
    return 76


def func3():
    return {'qeggk': 54, 'jpkym': 47, 'iihxm': 56}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 86.27


b = ["Hello"]
b[0] = func4

f = b[0]()
