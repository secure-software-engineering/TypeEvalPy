# Functions are assigned as elements of a list and then called.


def func1():
    return 24.88


def func2():
    return [79, 79, 93]


def func3():
    return 'fkkbm'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'zyovc': 93, 'rqyoe': 42, 'yocvf': 2}


b = ["Hello"]
b[0] = func4

f = b[0]()
