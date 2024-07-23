# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return (83, 69, 60)


def func3():
    return 74.79


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [13, 2, 40]


b = ["Hello"]
b[0] = func4

f = b[0]()
