# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [4, 63, 62]


def func2():
    return 'zvamd'


def func3():
    return {'todlc': 29, 'fpsmu': 16, 'oiifm': 71}


def func4():
    return 42


def func5():
    return 60.63


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
