# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [53, 76, 49]


def func2():
    return 47.0


def func3():
    return {'wzohs': 97, 'harbq': 95, 'uagxb': 10}


def func4():
    return (80, 95, 70)


def func5():
    return 'smyie'


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
