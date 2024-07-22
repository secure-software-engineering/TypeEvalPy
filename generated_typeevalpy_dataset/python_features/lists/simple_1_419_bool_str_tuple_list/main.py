# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 'cpevm'


def func3():
    return (97, 2, 4)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [2, 74, 25]


b = ["Hello"]
b[0] = func4

f = b[0]()
