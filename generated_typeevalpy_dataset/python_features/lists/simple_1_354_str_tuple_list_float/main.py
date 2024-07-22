# Functions are assigned as elements of a list and then called.


def func1():
    return 'kfzws'


def func2():
    return (94, 6, 76)


def func3():
    return [100, 100, 52]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 66.32


b = ["Hello"]
b[0] = func4

f = b[0]()
