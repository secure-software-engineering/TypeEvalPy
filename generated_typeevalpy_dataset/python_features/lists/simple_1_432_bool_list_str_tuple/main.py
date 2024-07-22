# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [97, 34, 65]


def func3():
    return 'anlpn'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (10, 40, 44)


b = ["Hello"]
b[0] = func4

f = b[0]()
