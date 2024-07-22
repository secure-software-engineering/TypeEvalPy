# Functions are assigned as elements of a list and then called.


def func1():
    return 'ydlvu'


def func2():
    return 37


def func3():
    return [60, 35, 87]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (14, 89, 87)


b = ["Hello"]
b[0] = func4

f = b[0]()
