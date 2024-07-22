# Functions are assigned as elements of a list and then called.


def func1():
    return [41, 65, 5]


def func2():
    return 82.8


def func3():
    return (21, 76, 9)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ospzg'


b = ["Hello"]
b[0] = func4

f = b[0]()
