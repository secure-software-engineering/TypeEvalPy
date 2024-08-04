# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return [83, 34, 28]


def func3():
    return (75, 82, 84)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ninne'


b = ["Hello"]
b[0] = func4

f = b[0]()
