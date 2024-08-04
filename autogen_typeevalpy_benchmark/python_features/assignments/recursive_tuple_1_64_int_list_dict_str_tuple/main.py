# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return [38, 12, 15]


def func3():
    return {'ctytd': 47, 'jwyoa': 87, 'bnwzi': 17}


def func4():
    return 'npfkn'


def func5():
    return (59, 41, 19)


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
