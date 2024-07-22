# Functions are assigned as elements of a list and then called.


def func1():
    return (54, 89, 93)


def func2():
    return 72.25


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [55, 50, 13]


b = ["Hello"]
b[0] = func4

f = b[0]()