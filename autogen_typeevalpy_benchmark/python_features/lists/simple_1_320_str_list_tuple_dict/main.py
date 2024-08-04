# Functions are assigned as elements of a list and then called.


def func1():
    return 'actir'


def func2():
    return [29, 12, 72]


def func3():
    return (73, 15, 5)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'aqpek': 23, 'vdwdq': 52, 'grouq': 100}


b = ["Hello"]
b[0] = func4

f = b[0]()
