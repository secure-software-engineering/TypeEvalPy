# Functions are assigned as elements of a list and then called.


def func1():
    return 50.98


def func2():
    return {'lquat': 42, 'qsqim': 70, 'jbzku': 24}


def func3():
    return [71, 30, 50]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 65


b = ["Hello"]
b[0] = func4

f = b[0]()
