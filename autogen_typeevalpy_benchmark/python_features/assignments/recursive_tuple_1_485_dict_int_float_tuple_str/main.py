# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wybxx': 80, 'tnpsm': 74, 'cutte': 14}


def func2():
    return 99


def func3():
    return 89.01


def func4():
    return (19, 38, 63)


def func5():
    return 'jgnrd'


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
