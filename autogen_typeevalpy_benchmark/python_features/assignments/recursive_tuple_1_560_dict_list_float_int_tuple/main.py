# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'njmlt': 19, 'fvxxt': 57, 'iszhe': 54}


def func2():
    return [29, 82, 39]


def func3():
    return 38.9


def func4():
    return 4


def func5():
    return (14, 80, 12)


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
