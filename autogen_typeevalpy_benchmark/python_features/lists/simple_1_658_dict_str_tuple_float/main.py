# Functions are assigned as elements of a list and then called.


def func1():
    return {'ribil': 70, 'qeugc': 24, 'tkhvt': 91}


def func2():
    return 'lbxzi'


def func3():
    return (96, 56, 39)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61.64


b = ["Hello"]
b[0] = func4

f = b[0]()
