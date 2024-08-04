# Functions are assigned as elements of a list and then called.


def func1():
    return [14, 32, 99]


def func2():
    return 94


def func3():
    return 'ytzlh'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (8, 89, 53)


b = ["Hello"]
b[0] = func4

f = b[0]()
