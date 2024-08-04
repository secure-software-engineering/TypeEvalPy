# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'amuls'


def func2():
    return [89, 48, 82]


def func3():
    return 54.8


def func4():
    return {'kalsb': 24, 'cwrmn': 86, 'gydac': 26}


def func5():
    return (58, 85, 70)


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
