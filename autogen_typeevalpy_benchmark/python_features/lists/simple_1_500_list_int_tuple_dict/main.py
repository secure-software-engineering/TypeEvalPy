# Functions are assigned as elements of a list and then called.


def func1():
    return [21, 54, 20]


def func2():
    return 90


def func3():
    return (11, 17, 4)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'jjrsh': 62, 'usyhq': 82, 'dvzfk': 53}


b = ["Hello"]
b[0] = func4

f = b[0]()
