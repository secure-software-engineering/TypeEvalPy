# Functions are assigned as elements of a list and then called.


def func1():
    return 'vsajq'


def func2():
    return [57, 40, 59]


def func3():
    return (62, 26, 92)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 71.73


b = ["Hello"]
b[0] = func4

f = b[0]()
