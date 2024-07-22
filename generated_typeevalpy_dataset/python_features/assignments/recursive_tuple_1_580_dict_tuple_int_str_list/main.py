# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ynhcs': 94, 'lwxmo': 51, 'mprfd': 34}


def func2():
    return (65, 54, 81)


def func3():
    return 42


def func4():
    return 'opdky'


def func5():
    return [56, 22, 20]


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
