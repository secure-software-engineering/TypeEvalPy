# Functions are assigned as elements of a list and then called.


def func1():
    return [15, 12, 67]


def func2():
    return 'eoupd'


def func3():
    return (80, 52, 59)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52.5


b = ["Hello"]
b[0] = func4

f = b[0]()
