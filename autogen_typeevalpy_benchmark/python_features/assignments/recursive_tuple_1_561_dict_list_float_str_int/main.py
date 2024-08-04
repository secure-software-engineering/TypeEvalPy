# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'iamtq': 41, 'ftmdg': 97, 'okmke': 13}


def func2():
    return [96, 87, 17]


def func3():
    return 82.78


def func4():
    return 'relak'


def func5():
    return 54


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
