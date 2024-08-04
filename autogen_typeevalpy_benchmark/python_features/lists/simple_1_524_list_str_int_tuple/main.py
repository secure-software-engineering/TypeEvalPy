# Functions are assigned as elements of a list and then called.


def func1():
    return [52, 35, 18]


def func2():
    return 'jmtcm'


def func3():
    return 75


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (9, 1, 47)


b = ["Hello"]
b[0] = func4

f = b[0]()
