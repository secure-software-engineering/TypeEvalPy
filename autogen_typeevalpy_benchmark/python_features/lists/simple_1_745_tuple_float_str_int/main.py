# Functions are assigned as elements of a list and then called.


def func1():
    return (55, 83, 65)


def func2():
    return 26.22


def func3():
    return 'mzfjp'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 81


b = ["Hello"]
b[0] = func4

f = b[0]()
