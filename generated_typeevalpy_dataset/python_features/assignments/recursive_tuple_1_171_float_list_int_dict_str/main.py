# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 24.76


def func2():
    return [71, 61, 79]


def func3():
    return 47


def func4():
    return {'qtwgg': 22, 'rzitk': 38, 'seigg': 62}


def func5():
    return 'llzof'


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
