# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yfeou'


def func2():
    return {'ohpph': 50, 'npyrn': 88, 'shkwu': 22}


def func3():
    return 88.69


def func4():
    return 3


def func5():
    return [80, 86, 86]


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
