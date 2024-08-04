# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 11


def func2():
    return 'uycba'


def func3():
    return {'ffihv': 45, 'rhszz': 52, 'ttxah': 52}


def func4():
    return 82.36


def func5():
    return [97, 84, 2]


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
