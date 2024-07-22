# Functions are assigned as elements of a list and then called.


def func1():
    return 38.33


def func2():
    return 'vhjmu'


def func3():
    return [31, 15, 79]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (20, 3, 47)


b = ["Hello"]
b[0] = func4

f = b[0]()
