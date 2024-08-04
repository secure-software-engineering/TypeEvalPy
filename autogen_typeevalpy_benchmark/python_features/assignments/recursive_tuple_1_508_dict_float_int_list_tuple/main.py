# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jrtrb': 77, 'tiulg': 95, 'selre': 41}


def func2():
    return 42.0


def func3():
    return 35


def func4():
    return [24, 58, 64]


def func5():
    return (61, 41, 22)


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
