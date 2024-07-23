# Functions are assigned as elements of a list and then called.


def func1():
    return 9.13


def func2():
    return [43, 51, 60]


def func3():
    return 'lfmeo'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'anevr': 93, 'rvlwl': 19, 'mbeuv': 57}


b = ["Hello"]
b[0] = func4

f = b[0]()
