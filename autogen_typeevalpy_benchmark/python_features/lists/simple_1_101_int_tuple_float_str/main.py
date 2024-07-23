# Functions are assigned as elements of a list and then called.


def func1():
    return 23


def func2():
    return (90, 22, 82)


def func3():
    return 1.96


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'hupcm'


b = ["Hello"]
b[0] = func4

f = b[0]()
