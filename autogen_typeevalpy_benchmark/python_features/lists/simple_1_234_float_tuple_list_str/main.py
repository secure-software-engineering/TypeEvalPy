# Functions are assigned as elements of a list and then called.


def func1():
    return 16.71


def func2():
    return (60, 57, 97)


def func3():
    return [47, 75, 57]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dlcos'


b = ["Hello"]
b[0] = func4

f = b[0]()
