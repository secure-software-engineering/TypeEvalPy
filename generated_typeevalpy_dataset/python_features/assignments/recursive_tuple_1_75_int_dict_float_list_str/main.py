# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 93


def func2():
    return {'uqbgq': 98, 'eywim': 58, 'twnlg': 50}


def func3():
    return 47.04


def func4():
    return [88, 96, 47]


def func5():
    return 'abrml'


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
