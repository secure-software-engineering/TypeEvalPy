# Functions are assigned as elements of a list and then called.


def func1():
    return (26, 64, 41)


def func2():
    return [83, 17, 26]


def func3():
    return 'jltwv'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 97.06


b = ["Hello"]
b[0] = func4

f = b[0]()
