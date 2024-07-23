# Functions are assigned as elements of a list and then called.


def func1():
    return (90, 90, 26)


def func2():
    return 'tvchw'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [67, 74, 94]


b = ["Hello"]
b[0] = func4

f = b[0]()
