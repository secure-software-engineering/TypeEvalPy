# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hacle'


def func2():
    return {'zseqn': 11, 'vfxdj': 16, 'alijy': 10}


def func3():
    return 35.8


def func4():
    return 71


def func5():
    return (21, 46, 99)


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
