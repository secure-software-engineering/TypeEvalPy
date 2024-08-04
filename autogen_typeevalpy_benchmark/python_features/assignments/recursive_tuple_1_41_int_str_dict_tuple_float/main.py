# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9


def func2():
    return 'kxfwi'


def func3():
    return {'vreoi': 73, 'fslfz': 63, 'lvpgi': 59}


def func4():
    return (60, 74, 6)


def func5():
    return 73.99


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
