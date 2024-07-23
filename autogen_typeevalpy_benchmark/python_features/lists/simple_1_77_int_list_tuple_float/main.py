# Functions are assigned as elements of a list and then called.


def func1():
    return 67


def func2():
    return [65, 70, 20]


def func3():
    return (13, 38, 45)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 81.52


b = ["Hello"]
b[0] = func4

f = b[0]()
