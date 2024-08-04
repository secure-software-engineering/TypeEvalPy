# Functions are assigned as elements of a list and then called.


def func1():
    return 12.88


def func2():
    return 'fflgz'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'sobdc': 41, 'xgehh': 11, 'ejgxv': 86}


b = ["Hello"]
b[0] = func4

f = b[0]()
