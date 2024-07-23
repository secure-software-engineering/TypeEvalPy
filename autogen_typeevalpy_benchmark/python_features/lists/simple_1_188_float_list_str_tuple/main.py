# Functions are assigned as elements of a list and then called.


def func1():
    return 58.9


def func2():
    return [21, 53, 84]


def func3():
    return 'myaio'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (84, 99, 81)


b = ["Hello"]
b[0] = func4

f = b[0]()
