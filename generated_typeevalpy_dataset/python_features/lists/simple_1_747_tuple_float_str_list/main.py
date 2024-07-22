# Functions are assigned as elements of a list and then called.


def func1():
    return (78, 5, 82)


def func2():
    return 89.21


def func3():
    return 'cmhyp'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [100, 59, 50]


b = ["Hello"]
b[0] = func4

f = b[0]()
