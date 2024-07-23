# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50.21


def func2():
    return 18


def func3():
    return 'fuxfx'


def func4():
    return {'opxub': 87, 'hralt': 51, 'pmusa': 72}


def func5():
    return [26, 92, 4]


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
