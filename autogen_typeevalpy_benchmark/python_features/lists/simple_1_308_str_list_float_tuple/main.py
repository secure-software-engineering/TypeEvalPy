# Functions are assigned as elements of a list and then called.


def func1():
    return 'gvvzl'


def func2():
    return [26, 35, 27]


def func3():
    return 42.31


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (22, 57, 31)


b = ["Hello"]
b[0] = func4

f = b[0]()
