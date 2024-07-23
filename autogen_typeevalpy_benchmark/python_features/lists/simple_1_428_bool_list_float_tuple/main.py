# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return [49, 26, 36]


def func3():
    return 73.04


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 79, 28)


b = ["Hello"]
b[0] = func4

f = b[0]()
