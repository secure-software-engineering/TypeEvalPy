# Functions are assigned as elements of a list and then called.


def func1():
    return (27, 96, 40)


def func2():
    return [20, 5, 87]


def func3():
    return 12.02


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'mzfsh'


b = ["Hello"]
b[0] = func4

f = b[0]()
