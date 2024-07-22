# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (14, 41, 74)


def func2():
    return {'aeewp': 63, 'gqttz': 89, 'bwxfk': 26}


def func3():
    return [71, 95, 52]


def func4():
    return 45.02


def func5():
    return 'bjxsy'


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
