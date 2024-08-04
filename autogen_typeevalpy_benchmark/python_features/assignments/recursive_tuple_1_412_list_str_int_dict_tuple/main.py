# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 94, 86]


def func2():
    return 'jcpwc'


def func3():
    return 44


def func4():
    return {'smfbl': 52, 'gmfcb': 23, 'wjnhh': 15}


def func5():
    return (91, 26, 4)


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
