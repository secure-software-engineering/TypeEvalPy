# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tkryy': 70, 'bsmyq': 94, 'qmeun': 32}


def func2():
    return 62.13


def func3():
    return (72, 42, 92)


def func4():
    return [87, 42, 71]


def func5():
    return 42


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
