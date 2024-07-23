# Functions are assigned as elements of a list and then called.


def func1():
    return (35, 52, 6)


def func2():
    return 18


def func3():
    return 'akwky'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 30.67


b = ["Hello"]
b[0] = func4

f = b[0]()
