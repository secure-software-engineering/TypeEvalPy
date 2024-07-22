# Functions are assigned as elements of a list and then called.


def func1():
    return 'gndze'


def func2():
    return [61, 25, 16]


def func3():
    return 84.39


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (11, 19, 28)


b = ["Hello"]
b[0] = func4

f = b[0]()
