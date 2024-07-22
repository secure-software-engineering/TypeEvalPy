# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (6, 78, 69)


def func2():
    return [83, 30, 14]


def func3():
    return {'qergd': 51, 'aembh': 28, 'jbprx': 89}


def func4():
    return 54


def func5():
    return 22.94


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
