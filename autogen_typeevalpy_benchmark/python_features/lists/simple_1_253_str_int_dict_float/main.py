# Functions are assigned as elements of a list and then called.


def func1():
    return 'lfmhd'


def func2():
    return 73


def func3():
    return {'rqrsj': 54, 'lbgln': 53, 'lmskq': 18}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 95.39


b = ["Hello"]
b[0] = func4

f = b[0]()
