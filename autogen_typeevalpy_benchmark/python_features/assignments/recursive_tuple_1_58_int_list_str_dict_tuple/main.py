# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54


def func2():
    return [91, 43, 40]


def func3():
    return 'mkqos'


def func4():
    return {'rqqrm': 79, 'rmqkw': 67, 'gmsyd': 87}


def func5():
    return (42, 13, 53)


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
