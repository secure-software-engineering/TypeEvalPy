# Functions are assigned as elements of a list and then called.


def func1():
    return (90, 17, 1)


def func2():
    return 74


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52.7


b = ["Hello"]
b[0] = func4

f = b[0]()