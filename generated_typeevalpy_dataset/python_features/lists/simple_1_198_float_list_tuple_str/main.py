# Functions are assigned as elements of a list and then called.


def func1():
    return 15.64


def func2():
    return [80, 75, 42]


def func3():
    return (72, 62, 29)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'aniqq'


b = ["Hello"]
b[0] = func4

f = b[0]()
