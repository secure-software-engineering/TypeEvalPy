# Functions are assigned as elements of a list and then called.


def func1():
    return (36, 75, 14)


def func2():
    return [86, 54, 62]


def func3():
    return 37.2


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'akorn'


b = ["Hello"]
b[0] = func4

f = b[0]()
