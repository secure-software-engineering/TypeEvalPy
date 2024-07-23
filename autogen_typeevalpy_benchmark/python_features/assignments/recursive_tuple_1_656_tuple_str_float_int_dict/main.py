# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (90, 7, 57)


def func2():
    return 'yjfnk'


def func3():
    return 28.24


def func4():
    return 42


def func5():
    return {'mpdmw': 68, 'ebdos': 27, 'nvcde': 23}


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
