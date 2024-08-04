# Functions are assigned as elements of a list and then called.


def func1():
    return (50, 37, 79)


def func2():
    return 'nizac'


def func3():
    return 35.37


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eisal': 94, 'jhrio': 47, 'hdmmb': 31}


b = ["Hello"]
b[0] = func4

f = b[0]()
