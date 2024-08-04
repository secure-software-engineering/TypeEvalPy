# Functions are assigned as elements of a list and then called.


def func1():
    return 74


def func2():
    return 56.29


def func3():
    return 'qashy'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [34, 98, 15]


b = ["Hello"]
b[0] = func4

f = b[0]()
