# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52.55


def func2():
    return [50, 47, 31]


def func3():
    return (84, 13, 98)


def func4():
    return 'yimlu'


def func5():
    return {'spbln': 71, 'fnzrv': 35, 'foubu': 91}


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
