# Functions are assigned as elements of a list and then called.


def func1():
    return 47.22


def func2():
    return {'nqkyv': 74, 'eieyu': 43, 'bvmdn': 62}


def func3():
    return [5, 91, 69]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (7, 35, 48)


b = ["Hello"]
b[0] = func4

f = b[0]()
