# Functions are assigned as elements of a list and then called.


def func1():
    return 'larzl'


def func2():
    return [61, 17, 29]


def func3():
    return 99


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (19, 41, 63)


b = ["Hello"]
b[0] = func4

f = b[0]()
