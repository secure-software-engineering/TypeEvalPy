# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 25, 66)


def func2():
    return 47


def func3():
    return {'rkoyh': 14, 'pczkr': 82, 'zovch': 16}


def func4():
    return [51, 80, 79]


def func5():
    return 'fvnoy'


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
