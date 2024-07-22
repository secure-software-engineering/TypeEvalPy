# Functions are assigned as elements of a list and then called.


def func1():
    return 10


def func2():
    return 30.19


def func3():
    return 'xnxdd'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (54, 4, 42)


b = ["Hello"]
b[0] = func4

f = b[0]()
