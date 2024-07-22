# Functions are assigned as elements of a list and then called.


def func1():
    return 88


def func2():
    return 'olhlp'


def func3():
    return (39, 40, 69)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [4, 30, 13]


b = ["Hello"]
b[0] = func4

f = b[0]()
