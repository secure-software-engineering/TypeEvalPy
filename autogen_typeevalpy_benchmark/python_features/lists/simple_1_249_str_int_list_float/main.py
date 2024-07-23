# Functions are assigned as elements of a list and then called.


def func1():
    return 'blcep'


def func2():
    return 88


def func3():
    return [17, 100, 47]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 21.86


b = ["Hello"]
b[0] = func4

f = b[0]()
