# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'bjacc': 44, 'yvzfi': 48, 'ulmuf': 50}


def func2():
    return 'buadu'


def func3():
    return 33


def func4():
    return 8.12


def func5():
    return [2, 11, 87]


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
