# Functions are assigned as elements of a list and then called.


def func1():
    return 15.57


def func2():
    return {'syuel': 90, 'yzuqf': 75, 'itmmg': 40}


def func3():
    return 39


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'rqqcv'


b = ["Hello"]
b[0] = func4

f = b[0]()
