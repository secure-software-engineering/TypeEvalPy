# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54


def func2():
    return (42, 66, 12)


def func3():
    return {'ifliv': 46, 'dufas': 48, 'ghaec': 36}


def func4():
    return 'nzxcf'


def func5():
    return [3, 90, 64]


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
