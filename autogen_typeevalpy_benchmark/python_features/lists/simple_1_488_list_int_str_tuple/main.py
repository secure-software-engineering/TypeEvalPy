# Functions are assigned as elements of a list and then called.


def func1():
    return [66, 64, 31]


def func2():
    return 29


def func3():
    return 'himea'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (78, 22, 68)


b = ["Hello"]
b[0] = func4

f = b[0]()
