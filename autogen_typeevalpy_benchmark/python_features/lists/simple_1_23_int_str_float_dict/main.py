# Functions are assigned as elements of a list and then called.


def func1():
    return 53


def func2():
    return 'alixm'


def func3():
    return 56.38


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rjxud': 80, 'utzix': 3, 'ntqnc': 45}


b = ["Hello"]
b[0] = func4

f = b[0]()
