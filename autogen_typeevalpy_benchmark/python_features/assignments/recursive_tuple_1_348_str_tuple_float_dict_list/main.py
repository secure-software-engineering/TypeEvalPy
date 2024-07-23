# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ikhlg'


def func2():
    return (57, 13, 73)


def func3():
    return 91.38


def func4():
    return {'pmlbu': 14, 'qkgwv': 40, 'fomxt': 9}


def func5():
    return [36, 2, 69]


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
