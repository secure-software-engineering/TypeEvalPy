# Functions are assigned as elements of a list and then called.


def func1():
    return {'devpt': 62, 'dosyx': 13, 'gejkj': 45}


def func2():
    return 'cdkeo'


def func3():
    return (80, 38, 56)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 63, 45]


b = ["Hello"]
b[0] = func4

f = b[0]()
