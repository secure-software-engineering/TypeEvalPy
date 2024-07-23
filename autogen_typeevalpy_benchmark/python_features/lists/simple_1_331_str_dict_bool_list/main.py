# Functions are assigned as elements of a list and then called.


def func1():
    return 'wvcvm'


def func2():
    return {'mskxk': 86, 'unzep': 96, 'dequv': 79}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [49, 44, 6]


b = ["Hello"]
b[0] = func4

f = b[0]()
