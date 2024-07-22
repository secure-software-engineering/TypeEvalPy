# Functions are assigned as elements of a list and then called.


def func1():
    return 65.42


def func2():
    return (69, 55, 37)


def func3():
    return [3, 26, 71]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
