# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30.6


def func2():
    return 'xiqkt'


def func3():
    return 14


def func4():
    return (1, 11, 29)


def func5():
    return {'lmtqj': 51, 'lygyw': 41, 'ufkpr': 44}


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
