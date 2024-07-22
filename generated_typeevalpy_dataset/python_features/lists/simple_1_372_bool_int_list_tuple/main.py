# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 75


def func3():
    return [26, 3, 75]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (81, 46, 52)


b = ["Hello"]
b[0] = func4

f = b[0]()
