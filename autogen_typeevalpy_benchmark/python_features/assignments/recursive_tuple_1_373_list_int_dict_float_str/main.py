# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 42, 21]


def func2():
    return 1


def func3():
    return {'ndrah': 62, 'xkhuu': 63, 'oelzw': 32}


def func4():
    return 47.52


def func5():
    return 'okyuf'


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
