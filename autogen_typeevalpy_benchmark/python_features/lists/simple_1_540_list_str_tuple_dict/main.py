# Functions are assigned as elements of a list and then called.


def func1():
    return [72, 64, 3]


def func2():
    return 'zrnnb'


def func3():
    return (58, 34, 89)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'prkml': 23, 'imrnl': 3, 'mvndl': 26}


b = ["Hello"]
b[0] = func4

f = b[0]()
