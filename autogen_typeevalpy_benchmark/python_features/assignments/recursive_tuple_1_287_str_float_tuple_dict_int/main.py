# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'haddl'


def func2():
    return 93.29


def func3():
    return (27, 16, 82)


def func4():
    return {'traym': 20, 'acgwp': 28, 'ohsmt': 9}


def func5():
    return 51


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
