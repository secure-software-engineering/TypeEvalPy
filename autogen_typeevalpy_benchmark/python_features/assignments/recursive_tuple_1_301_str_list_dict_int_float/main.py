# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nzogt'


def func2():
    return [81, 47, 29]


def func3():
    return {'vktbi': 66, 'kfsjl': 53, 'vfxmy': 83}


def func4():
    return 97


def func5():
    return 63.9


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
