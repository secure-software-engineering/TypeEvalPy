# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hmrhl'


def func2():
    return [98, 98, 61]


def func3():
    return {'nkyvz': 4, 'xwwow': 49, 'goclc': 42}


def func4():
    return 42.68


def func5():
    return (29, 87, 33)


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
