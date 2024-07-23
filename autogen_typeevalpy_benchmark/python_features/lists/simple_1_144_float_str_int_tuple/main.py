# Functions are assigned as elements of a list and then called.


def func1():
    return 89.74


def func2():
    return 'cecec'


def func3():
    return 87


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (39, 38, 46)


b = ["Hello"]
b[0] = func4

f = b[0]()
