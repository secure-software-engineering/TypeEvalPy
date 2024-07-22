# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 31.72


def func3():
    return (24, 11, 17)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [98, 41, 28]


b = ["Hello"]
b[0] = func4

f = b[0]()