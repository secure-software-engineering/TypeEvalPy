# Functions are assigned as elements of a list and then called.


def func1():
    return (77, 45, 76)


def func2():
    return [36, 56, 18]


def func3():
    return 44


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 55.91


b = ["Hello"]
b[0] = func4

f = b[0]()
