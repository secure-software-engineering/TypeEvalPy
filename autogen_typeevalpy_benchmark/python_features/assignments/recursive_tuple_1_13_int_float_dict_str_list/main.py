# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return 29.94


def func3():
    return {'keyrq': 22, 'qkzkb': 32, 'vnlcj': 62}


def func4():
    return 'zouxj'


def func5():
    return [39, 77, 16]


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
