# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 63.13


def func3():
    return {'bpeyp': 72, 'nlofj': 75, 'aonea': 76}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 39


b = ["Hello"]
b[0] = func4

f = b[0]()
