# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wbpjb': 87, 'mgajg': 68, 'eelie': 64}


def func2():
    return 'jfryq'


def func3():
    return (90, 51, 60)


def func4():
    return 7


def func5():
    return 14.35


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
