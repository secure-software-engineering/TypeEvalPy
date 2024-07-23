# Functions are assigned as elements of a list and then called.


def func1():
    return [35, 43, 79]


def func2():
    return 'fgfjh'


def func3():
    return 93


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (28, 61, 37)


b = ["Hello"]
b[0] = func4

f = b[0]()
