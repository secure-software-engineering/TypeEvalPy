# Functions are assigned as elements of a list and then called.


def func1():
    return 61


def func2():
    return {'pcaek': 15, 'qmiwy': 65, 'pstla': 56}


def func3():
    return 'qkpjk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (13, 11, 95)


b = ["Hello"]
b[0] = func4

f = b[0]()
