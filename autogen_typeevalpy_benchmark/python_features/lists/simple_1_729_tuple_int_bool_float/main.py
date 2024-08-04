# Functions are assigned as elements of a list and then called.


def func1():
    return (5, 37, 23)


def func2():
    return 100


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 25.74


b = ["Hello"]
b[0] = func4

f = b[0]()
