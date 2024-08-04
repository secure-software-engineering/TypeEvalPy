# Functions are assigned as elements of a list and then called.


def func1():
    return (92, 30, 69)


def func2():
    return 30


def func3():
    return [25, 36, 90]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wqyii'


b = ["Hello"]
b[0] = func4

f = b[0]()
