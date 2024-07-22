# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [40, 59, 17]


def func2():
    return 23


def func3():
    return {'wrmuq': 90, 'pkkpi': 92, 'pbmxz': 22}


def func4():
    return 40.31


def func5():
    return (52, 83, 94)


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
