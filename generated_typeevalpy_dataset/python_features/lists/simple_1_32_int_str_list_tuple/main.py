# Functions are assigned as elements of a list and then called.


def func1():
    return 62


def func2():
    return 'urerv'


def func3():
    return [61, 35, 76]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (74, 20, 83)


b = ["Hello"]
b[0] = func4

f = b[0]()
