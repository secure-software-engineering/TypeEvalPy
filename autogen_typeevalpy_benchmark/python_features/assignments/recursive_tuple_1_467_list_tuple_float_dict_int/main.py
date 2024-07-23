# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [67, 84, 53]


def func2():
    return (56, 14, 43)


def func3():
    return 19.23


def func4():
    return {'bzwpe': 47, 'ieoig': 95, 'hbpzn': 46}


def func5():
    return 39


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
