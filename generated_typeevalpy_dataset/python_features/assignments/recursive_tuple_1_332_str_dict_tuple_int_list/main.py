# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rwphn'


def func2():
    return {'cjwvr': 83, 'lgbtu': 88, 'snktu': 52}


def func3():
    return (64, 62, 64)


def func4():
    return 54


def func5():
    return [27, 30, 63]


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