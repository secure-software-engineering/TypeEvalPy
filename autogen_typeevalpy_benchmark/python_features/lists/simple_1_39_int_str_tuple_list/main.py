# Functions are assigned as elements of a list and then called.


def func1():
    return 41


def func2():
    return 'mkbzs'


def func3():
    return (77, 5, 19)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [68, 4, 45]


b = ["Hello"]
b[0] = func4

f = b[0]()
