# Functions are assigned as elements of a list and then called.


def func1():
    return 'wybyc'


def func2():
    return 87.94


def func3():
    return {'akmmd': 19, 'bbhlh': 24, 'jysyn': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [80, 8, 96]


b = ["Hello"]
b[0] = func4

f = b[0]()
