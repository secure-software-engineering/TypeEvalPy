# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 78, 17]


def func2():
    return {'msehn': 72, 'rksyj': 60, 'dggnr': 56}


def func3():
    return (72, 91, 29)


def func4():
    return 99


def func5():
    return 'tyxvl'


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
