# Functions are assigned as elements of a list and then called.


def func1():
    return 'rddme'


def func2():
    return [11, 40, 17]


def func3():
    return (19, 57, 40)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 3.82


b = ["Hello"]
b[0] = func4

f = b[0]()
