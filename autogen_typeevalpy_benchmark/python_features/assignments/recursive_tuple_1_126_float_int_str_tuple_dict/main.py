# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.35


def func2():
    return 79


def func3():
    return 'nrpwa'


def func4():
    return (93, 31, 98)


def func5():
    return {'djscg': 50, 'wmwrd': 25, 'muqui': 81}


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
