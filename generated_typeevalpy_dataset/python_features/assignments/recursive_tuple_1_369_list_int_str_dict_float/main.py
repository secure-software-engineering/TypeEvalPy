# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [55, 35, 94]


def func2():
    return 47


def func3():
    return 'ifcvq'


def func4():
    return {'gbcrc': 6, 'knbzs': 85, 'ngton': 18}


def func5():
    return 70.35


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
