# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vvyrc'


def func2():
    return (85, 50, 48)


def func3():
    return [45, 32, 51]


def func4():
    return {'jhujp': 45, 'rdjra': 18, 'lvpbz': 50}


def func5():
    return 58.17


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
