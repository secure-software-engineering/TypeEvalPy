# Functions are assigned as elements of a list and then called.


def func1():
    return 46.29


def func2():
    return 'ktmsw'


def func3():
    return (83, 39, 24)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [2, 31, 14]


b = ["Hello"]
b[0] = func4

f = b[0]()
