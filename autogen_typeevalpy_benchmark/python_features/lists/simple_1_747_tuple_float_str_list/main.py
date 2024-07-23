# Functions are assigned as elements of a list and then called.


def func1():
    return (57, 12, 88)


def func2():
    return 29.09


def func3():
    return 'uloof'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [95, 85, 81]


b = ["Hello"]
b[0] = func4

f = b[0]()
