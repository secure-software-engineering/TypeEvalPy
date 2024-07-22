# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9.63


def func2():
    return [75, 61, 20]


def func3():
    return 'kawbj'


def func4():
    return 59


def func5():
    return {'mgyim': 82, 'lqxlr': 7, 'pncta': 14}


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
