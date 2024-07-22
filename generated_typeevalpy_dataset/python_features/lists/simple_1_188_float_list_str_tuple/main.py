# Functions are assigned as elements of a list and then called.


def func1():
    return 63.87


def func2():
    return [49, 60, 60]


def func3():
    return 'evvdq'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (55, 63, 37)


b = ["Hello"]
b[0] = func4

f = b[0]()
