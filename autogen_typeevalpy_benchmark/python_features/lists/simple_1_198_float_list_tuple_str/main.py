# Functions are assigned as elements of a list and then called.


def func1():
    return 84.14


def func2():
    return [46, 41, 1]


def func3():
    return (20, 50, 77)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'hjjnf'


b = ["Hello"]
b[0] = func4

f = b[0]()
