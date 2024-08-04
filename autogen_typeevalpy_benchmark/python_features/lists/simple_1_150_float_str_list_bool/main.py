# Functions are assigned as elements of a list and then called.


def func1():
    return 60.64


def func2():
    return 'gyfzh'


def func3():
    return [35, 7, 68]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
