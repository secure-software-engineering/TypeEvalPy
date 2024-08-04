# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89.55


def func2():
    return {'flgpz': 1, 'uzncp': 96, 'ixemz': 5}


def func3():
    return [88, 87, 53]


def func4():
    return 67


def func5():
    return 'zwbkg'


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
