# Functions are assigned as elements of a list and then called.


def func1():
    return [81, 5, 100]


def func2():
    return 54


def func3():
    return (51, 68, 81)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 19.37


b = ["Hello"]
b[0] = func4

f = b[0]()
