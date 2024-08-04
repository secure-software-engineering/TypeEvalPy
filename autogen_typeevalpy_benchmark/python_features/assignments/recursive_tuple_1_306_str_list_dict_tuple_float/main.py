# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ubwho'


def func2():
    return [35, 17, 13]


def func3():
    return {'yrfxo': 31, 'aiqhl': 20, 'fqogo': 3}


def func4():
    return (71, 75, 41)


def func5():
    return 76.47


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
