# Functions are assigned as elements of a list and then called.


def func1():
    return [91, 81, 53]


def func2():
    return 'hjili'


def func3():
    return (83, 2, 84)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22.46


b = ["Hello"]
b[0] = func4

f = b[0]()
