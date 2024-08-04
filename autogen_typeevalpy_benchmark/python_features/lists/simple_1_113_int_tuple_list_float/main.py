# Functions are assigned as elements of a list and then called.


def func1():
    return 42


def func2():
    return (23, 41, 84)


def func3():
    return [1, 9, 73]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 9.68


b = ["Hello"]
b[0] = func4

f = b[0]()
