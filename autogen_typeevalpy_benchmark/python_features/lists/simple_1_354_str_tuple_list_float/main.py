# Functions are assigned as elements of a list and then called.


def func1():
    return 'bhbil'


def func2():
    return (93, 89, 69)


def func3():
    return [27, 94, 47]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 60.91


b = ["Hello"]
b[0] = func4

f = b[0]()
