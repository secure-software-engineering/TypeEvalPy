# Functions are assigned as elements of a list and then called.


def func1():
    return {'cvssh': 89, 'phowg': 87, 'pendl': 77}


def func2():
    return (11, 74, 85)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'oqnfr'


b = ["Hello"]
b[0] = func4

f = b[0]()
