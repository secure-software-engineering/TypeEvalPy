# Functions are assigned as elements of a list and then called.


def func1():
    return (96, 70, 7)


def func2():
    return [56, 50, 58]


def func3():
    return 'xjslq'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 79.75


b = ["Hello"]
b[0] = func4

f = b[0]()
