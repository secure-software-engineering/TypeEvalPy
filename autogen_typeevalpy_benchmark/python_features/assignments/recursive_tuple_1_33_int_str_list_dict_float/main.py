# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 39


def func2():
    return 'gpiin'


def func3():
    return [41, 31, 63]


def func4():
    return {'gberc': 95, 'tvpdb': 4, 'abmgl': 21}


def func5():
    return 39.0


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
