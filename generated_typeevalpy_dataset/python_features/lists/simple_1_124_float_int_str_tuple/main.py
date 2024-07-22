# Functions are assigned as elements of a list and then called.


def func1():
    return 86.03


def func2():
    return 13


def func3():
    return 'mcihe'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (26, 51, 45)


b = ["Hello"]
b[0] = func4

f = b[0]()
