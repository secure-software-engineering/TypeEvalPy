# Functions are assigned as elements of a list and then called.


def func1():
    return 'rhspk'


def func2():
    return (27, 3, 54)


def func3():
    return [64, 83, 11]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 24


b = ["Hello"]
b[0] = func4

f = b[0]()
