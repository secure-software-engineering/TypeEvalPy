# Functions are assigned as elements of a list and then called.


def func1():
    return (1, 61, 28)


def func2():
    return 'ajgdo'


def func3():
    return 47


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [83, 51, 56]


b = ["Hello"]
b[0] = func4

f = b[0]()
