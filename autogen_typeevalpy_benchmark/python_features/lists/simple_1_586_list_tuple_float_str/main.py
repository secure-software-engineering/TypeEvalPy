# Functions are assigned as elements of a list and then called.


def func1():
    return [12, 23, 70]


def func2():
    return (78, 73, 48)


def func3():
    return 12.47


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cvzxt'


b = ["Hello"]
b[0] = func4

f = b[0]()
