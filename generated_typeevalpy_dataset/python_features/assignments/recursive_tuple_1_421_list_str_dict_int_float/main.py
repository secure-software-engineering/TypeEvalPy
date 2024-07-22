# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [47, 55, 35]


def func2():
    return 'ggywg'


def func3():
    return {'nnpcx': 28, 'lgbxd': 19, 'ijhkq': 82}


def func4():
    return 98


def func5():
    return 85.4


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
