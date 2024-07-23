# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return 15.12


def func3():
    return 'vhtzo'


def func4():
    return (18, 100, 6)


def func5():
    return {'vyxhy': 49, 'hflji': 9, 'ofmlr': 33}


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
