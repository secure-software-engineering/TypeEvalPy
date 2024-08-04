# Functions are assigned as elements of a list and then called.


def func1():
    return 'qaizm'


def func2():
    return (56, 22, 10)


def func3():
    return [54, 28, 33]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 51.09


b = ["Hello"]
b[0] = func4

f = b[0]()
