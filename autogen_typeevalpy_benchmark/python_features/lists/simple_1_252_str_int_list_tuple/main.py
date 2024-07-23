# Functions are assigned as elements of a list and then called.


def func1():
    return 'tiwev'


def func2():
    return 97


def func3():
    return [41, 42, 97]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (46, 8, 66)


b = ["Hello"]
b[0] = func4

f = b[0]()
