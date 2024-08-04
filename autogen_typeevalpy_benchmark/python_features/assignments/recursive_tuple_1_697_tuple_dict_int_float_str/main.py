# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (96, 10, 80)


def func2():
    return {'pgdyu': 62, 'gxyhg': 73, 'ebibb': 86}


def func3():
    return 13


def func4():
    return 49.08


def func5():
    return 'ypfob'


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
