# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7.64


def func2():
    return (10, 73, 12)


def func3():
    return 72


def func4():
    return [100, 15, 69]


def func5():
    return {'enwom': 24, 'qebrv': 83, 'mxzdi': 74}


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
