# Functions are assigned as elements of a list and then called.


def func1():
    return (70, 51, 83)


def func2():
    return 39


def func3():
    return 'ilepr'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [17, 43, 34]


b = ["Hello"]
b[0] = func4

f = b[0]()
