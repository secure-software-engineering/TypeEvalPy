# Functions are assigned as elements of a list and then called.


def func1():
    return 84


def func2():
    return [18, 100, 31]


def func3():
    return 'onhnr'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77.61


b = ["Hello"]
b[0] = func4

f = b[0]()
