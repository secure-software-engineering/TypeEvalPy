# Functions are assigned as elements of a list and then called.


def func1():
    return 50


def func2():
    return 5.52


def func3():
    return [25, 99, 96]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'jxqpk'


b = ["Hello"]
b[0] = func4

f = b[0]()
