# Functions are assigned as elements of a list and then called.


def func1():
    return [93, 21, 53]


def func2():
    return {'tcomt': 39, 'ejbiu': 1, 'xdgej': 86}


def func3():
    return 45


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 79.94


b = ["Hello"]
b[0] = func4

f = b[0]()
