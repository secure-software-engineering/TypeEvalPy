# Functions are assigned as elements of a list and then called.


def func1():
    return 'qoamd'


def func2():
    return True


def func3():
    return (57, 98, 69)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wsjzh': 56, 'nbdlm': 63, 'jaczl': 17}


b = ["Hello"]
b[0] = func4

f = b[0]()
